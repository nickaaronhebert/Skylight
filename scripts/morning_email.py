#!/usr/bin/env python3
"""
Daily morning digest email for the household.

Usage:
  python3 scripts/morning_email.py --gmail-password <app_password>
  python3 scripts/morning_email.py --gmail-password <app_password> --date 2026-05-13
  python3 scripts/morning_email.py --gmail-password <app_password> --preview

Token is loaded automatically from ~/.skylight_tokens.json and refreshed as needed.
"""

import argparse
import json
import os
import smtplib
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, timezone
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

FRAME_ID = "5289925"
BASE_URL = "https://app.ourskylight.com"
FROM_EMAIL = "nickaaronhebert@gmail.com"
TO_EMAILS = ["madison.stillwell@gmail.com", "nick@telegramd.com"]
GMAIL_SMTP = "smtp.gmail.com"
GMAIL_PORT = 587

MEAL_CATEGORIES = {
    "8837086": "Breakfast",
    "8837087": "Lunch",
    "8837088": "Dinner",
    "8837089": "Snack",
}

PEOPLE = {
    "20235057": {"name": "Eleanor",          "color": "#93D1E6", "emoji": "👧"},
    "20235070": {"name": "Delaney",          "color": "#FBA994", "emoji": "👧"},
    "20235082": {"name": "Marley",           "color": "#D5B6EC", "emoji": "👧"},
    "20235149": {"name": "Elizabeth",        "color": "#408257", "emoji": "🏠"},
    "20237876": {"name": "Evening Assistant","color": "#FDB305", "emoji": "🌙"},
}

TOKEN_FILE = os.path.expanduser("~/.skylight_tokens.json")
OAUTH_URL = "https://app.ourskylight.com/oauth/token"

HEADERS = {
    "Authorization": "",
    "Accept": "application/json",
    "skylight-api-version": "2026-04-15",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
}


def load_token() -> str:
    """Load access token from file, refreshing it if expired."""
    if not os.path.exists(TOKEN_FILE):
        print(f"ERROR: Token file not found at {TOKEN_FILE}", file=sys.stderr)
        sys.exit(1)

    with open(TOKEN_FILE) as f:
        tokens = json.load(f)

    # Refresh if expired or expiring within 5 minutes
    if time.time() >= tokens.get("expires_at", 0) - 300:
        tokens = _refresh_token(tokens["refresh_token"])

    return tokens["access_token"]


def _refresh_token(refresh_token: str) -> dict:
    """Exchange refresh token for a new access token and save to file."""
    body = urllib.parse.urlencode({
        "grant_type": "refresh_token",
        "client_id": "skylight-mobile",
        "refresh_token": refresh_token,
    }).encode()

    req = urllib.request.Request(OAUTH_URL, data=body, headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://ourskylight.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
    })

    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"ERROR: Token refresh failed: {e.read().decode()}", file=sys.stderr)
        sys.exit(1)

    tokens = {
        "access_token": data["access_token"],
        "refresh_token": data["refresh_token"],
        "expires_at": time.time() + data["expires_in"],
    }

    with open(TOKEN_FILE, "w") as f:
        json.dump(tokens, f, indent=2)

    print("Token refreshed.")
    return tokens


def fetch(path: str, token: str) -> dict:
    HEADERS["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(f"{BASE_URL}{path}", headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def _meal_matches_day(item: dict, day: str, target_weekday: str) -> bool:
    """Return True if this meal sitting applies to the target day.

    One-off meals store their date(s) in 'instances' — check for an exact match.
    Recurring meals have an rrule with BYDAY — match the weekday.
    """
    a = item["attributes"]
    instances = a.get("instances") or []
    rrule = a.get("rrule") or ""

    if instances:
        return day in instances

    # Recurring — match by day of week via BYDAY
    for part in rrule.split(";"):
        if part.startswith("BYDAY="):
            byday = part.split("=", 1)[1].upper()
            return target_weekday in byday.split(",")

    return False


def fetch_meals(token: str, day: str) -> dict:
    from datetime import timedelta
    dt = datetime.strptime(day, "%Y-%m-%d")
    # Query the full surrounding week so the API populates 'instances' correctly
    date_min = (dt - timedelta(days=7)).strftime("%Y-%m-%d")
    date_max = (dt + timedelta(days=7)).strftime("%Y-%m-%d")

    data = fetch(
        f"/api/frames/{FRAME_ID}/meals/sittings"
        f"?date_min={date_min}&date_max={date_max}&include=meal_category,meal_recipe",
        token
    )
    weekday = dt.strftime("%a")[:2].upper()

    meals = {"Breakfast": [], "Lunch": [], "Dinner": [], "Snack": []}
    for item in data.get("data", []):
        if not _meal_matches_day(item, day, weekday):
            continue
        cat_id = item["relationships"]["meal_category"]["data"]["id"]
        cat_name = MEAL_CATEGORIES.get(cat_id, "Other")
        meals[cat_name].append(item["attributes"]["summary"])
    return meals


def fetch_events(token: str, day: str) -> list:
    # Query ±1 day in UTC to catch events whose UTC date differs from local date
    from datetime import timedelta
    dt = datetime.strptime(day, "%Y-%m-%d")
    date_min = (dt - timedelta(days=1)).strftime("%Y-%m-%d")
    date_max = (dt + timedelta(days=2)).strftime("%Y-%m-%d")

    data = fetch(
        f"/api/frames/{FRAME_ID}/calendar_events"
        f"?date_min={date_min}&date_max={date_max}",
        token
    )

    target = datetime.strptime(day, "%Y-%m-%d").date()
    events = []
    for item in data.get("data", []):
        a = item["attributes"]
        if a.get("all_day"):
            time_str = "All day"
            local_date = target  # include all-day events on the target day
        else:
            try:
                starts = datetime.fromisoformat(a["starts_at"].replace("Z", "+00:00"))
                local = starts.astimezone()
                local_date = local.date()
                time_str = local.strftime("%-I:%M %p")
            except Exception:
                continue

        if local_date != target:
            continue

        events.append({
            "summary": a.get("summary", "Untitled"),
            "time": time_str,
            "location": a.get("location") or "",
            "_sort": time_str,
        })

    events.sort(key=lambda e: e["_sort"])
    return events


def fetch_chores(token: str, day: str) -> dict:
    data = fetch(
        f"/api/frames/{FRAME_ID}/chores"
        f"?after={day}&before={day}&include_late=true",
        token
    )
    chores = {pid: {"done": [], "pending": []} for pid in PEOPLE}
    for chore in data.get("data", []):
        cat_id = chore["relationships"]["category"]["data"]["id"]
        if cat_id not in PEOPLE:
            continue
        status = chore["attributes"]["status"]
        summary = chore["attributes"]["summary"]
        if status == "complete":
            chores[cat_id]["done"].append(summary)
        else:
            chores[cat_id]["pending"].append(summary)
    return chores


def meal_row(label: str, items: list) -> str:
    if not items:
        return ""
    value = " · ".join(items)
    return f"""
        <tr>
            <td style="padding:6px 12px 6px 0; color:#888; font-size:13px; white-space:nowrap; vertical-align:top;">{label}</td>
            <td style="padding:6px 0; font-size:14px; color:#222;">{value}</td>
        </tr>"""


def chore_list(items: list, done: bool) -> str:
    if not items:
        return ""
    color = "#27ae60" if done else "#555"
    icon = "✓" if done else "·"
    rows = "".join(
        f'<li style="margin:3px 0; color:{color};">{icon} {item}</li>'
        for item in items
    )
    return f'<ul style="margin:4px 0 8px 0; padding-left:16px; list-style:none;">{rows}</ul>'


def person_card(cat_id: str, chores: dict) -> str:
    person = PEOPLE[cat_id]
    done = chores[cat_id]["done"]
    pending = chores[cat_id]["pending"]
    total = len(done) + len(pending)
    if total == 0:
        return ""
    pct = int(len(done) / total * 100) if total > 0 else 0
    bar_filled = int(pct / 10)
    bar = "█" * bar_filled + "░" * (10 - bar_filled)

    return f"""
    <div style="margin-bottom:16px; border-left:4px solid {person['color']}; padding-left:12px;">
        <div style="font-weight:600; font-size:14px; color:#222; margin-bottom:4px;">
            {person['emoji']} {person['name']}
            <span style="font-weight:400; color:#888; font-size:12px; margin-left:8px;">
                {bar} {pct}% &nbsp;({len(done)}/{total})
            </span>
        </div>
        {chore_list(done, done=True)}
        {chore_list(pending, done=False)}
    </div>"""


def events_section(events: list) -> str:
    if not events:
        return ""
    rows = "".join(f"""
        <tr>
            <td style="padding:6px 12px 6px 0; color:#888; font-size:13px; white-space:nowrap; vertical-align:top;">{e['time']}</td>
            <td style="padding:6px 0; font-size:14px; color:#222;">
                {e['summary']}
                {"<br><span style='font-size:12px;color:#aaa;'>" + e['location'] + "</span>" if e['location'] else ""}
            </td>
        </tr>""" for e in events)
    return f"""
    <div style="margin-bottom:28px;">
        <div style="font-size:13px; font-weight:700; text-transform:uppercase;
                    letter-spacing:1px; color:#888; margin-bottom:10px;">Today's Events</div>
        <table>{rows}</table>
    </div>"""


def build_html(day: str, meals: dict, chores: dict, events: list) -> str:
    dt = datetime.strptime(day, "%Y-%m-%d")
    day_label = dt.strftime("%A, %B %-d")

    meal_rows = (
        meal_row("Breakfast", meals["Breakfast"]) +
        meal_row("Lunch", meals["Lunch"]) +
        meal_row("Dinner", meals["Dinner"]) +
        meal_row("Snack", meals["Snack"])
    )

    has_meals = any(meals.values())
    meals_section = f"""
    <div style="margin-bottom:28px;">
        <div style="font-size:13px; font-weight:700; text-transform:uppercase;
                    letter-spacing:1px; color:#888; margin-bottom:10px;">Meals</div>
        {"<table>" + meal_rows + "</table>" if has_meals else
         '<p style="color:#aaa; font-size:13px;">No meals planned.</p>'}
    </div>""" if has_meals else ""

    people_cards = "".join(person_card(pid, chores) for pid in PEOPLE)

    return f"""
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"></head>
<body style="margin:0; padding:0; background:#f5f5f5; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;">
  <div style="max-width:540px; margin:32px auto; background:#fff;
              border-radius:8px; overflow:hidden; box-shadow:0 1px 4px rgba(0,0,0,0.08);">

    <!-- Header -->
    <div style="background:#222; padding:20px 24px;">
        <div style="font-size:11px; text-transform:uppercase; letter-spacing:2px; color:#888;">Daily Digest</div>
        <div style="font-size:22px; font-weight:700; color:#fff; margin-top:4px;">{day_label}</div>
    </div>

    <!-- Body -->
    <div style="padding:24px;">
        {events_section(events)}
        {meals_section}
        <div style="margin-bottom:12px;">
            <div style="font-size:13px; font-weight:700; text-transform:uppercase;
                        letter-spacing:1px; color:#888; margin-bottom:14px;">Chores & Tasks</div>
            {people_cards if people_cards.strip() else
             '<p style="color:#aaa; font-size:13px;">No tasks today.</p>'}
        </div>
    </div>

    <!-- Footer -->
    <div style="padding:14px 24px; background:#fafafa; border-top:1px solid #eee;
                font-size:11px; color:#bbb; text-align:center;">
        Skylight Daily Digest · {day}
    </div>
  </div>
</body>
</html>"""


def send_email(html: str, day: str, gmail_password: str):
    dt = datetime.strptime(day, "%Y-%m-%d")
    subject = f"Hebert Five - Daily Digest — {dt.strftime('%A, %B %-d')}"

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = FROM_EMAIL
    msg["To"] = ", ".join(TO_EMAILS)
    msg.attach(MIMEText(html, "html"))

    with smtplib.SMTP(GMAIL_SMTP, GMAIL_PORT) as server:
        server.ehlo()
        server.starttls()
        server.login(FROM_EMAIL, gmail_password)
        server.sendmail(FROM_EMAIL, TO_EMAILS, msg.as_string())


def main():
    parser = argparse.ArgumentParser(description="Send daily household digest email")
    parser.add_argument("--gmail-password", required=True, help="Gmail app password")
    parser.add_argument("--date", default=date.today().isoformat(), help="Date YYYY-MM-DD (default: today)")
    parser.add_argument("--preview", action="store_true", help="Print HTML instead of sending")
    args = parser.parse_args()

    try:
        datetime.strptime(args.date, "%Y-%m-%d")
    except ValueError:
        print("Date must be YYYY-MM-DD", file=sys.stderr)
        sys.exit(1)

    token = load_token()

    print(f"Fetching data for {args.date}...")
    meals = fetch_meals(token, args.date)
    chores = fetch_chores(token, args.date)
    events = fetch_events(token, args.date)

    html = build_html(args.date, meals, chores, events)

    if args.preview:
        print(html)
    else:
        print(f"Sending to {', '.join(TO_EMAILS)}...")
        send_email(html, args.date, args.gmail_password)
        print("Sent.")


if __name__ == "__main__":
    main()
