#!/usr/bin/env python3
"""
Evening recap email for the household — sent at 8:30 PM.

Shows today's chore completion by person, and a preview of tomorrow's
meals and events.

Usage:
  python3 scripts/evening_email.py --gmail-password <app_password>
  python3 scripts/evening_email.py --gmail-password <app_password> --date 2026-05-13
  python3 scripts/evening_email.py --gmail-password <app_password> --preview
"""

import argparse
import json
import smtplib
import sys
import urllib.request
from datetime import date, datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Re-use shared config from morning_email
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from morning_email import (
    load_token, fetch,
    fetch_chores, fetch_meals, fetch_events,
    FRAME_ID, BASE_URL, FROM_EMAIL, TO_EMAILS,
    GMAIL_SMTP, GMAIL_PORT, PEOPLE, MEAL_CATEGORIES,
)

def build_chore_summary(chores: dict) -> str:
    """Full chore completion recap by person."""
    cards = []
    for pid, person in PEOPLE.items():
        done = chores[pid]["done"]
        pending = chores[pid]["pending"]
        total = len(done) + len(pending)
        if total == 0:
            continue
        pct = int(len(done) / total * 100)
        bar = "█" * int(pct / 10) + "░" * (10 - int(pct / 10))

        done_rows = "".join(
            f'<li style="margin:3px 0; color:#27ae60;">✓ {t}</li>' for t in done
        )
        pending_rows = "".join(
            f'<li style="margin:3px 0; color:#e74c3c;">✗ {t}</li>' for t in pending
        )

        cards.append(f"""
    <div style="margin-bottom:16px; border-left:4px solid {person['color']}; padding-left:12px;">
        <div style="font-weight:600; font-size:14px; color:#222; margin-bottom:4px;">
            {person['emoji']} {person['name']}
            <span style="font-weight:400; color:#888; font-size:12px; margin-left:8px;">
                {bar} {pct}% &nbsp;({len(done)}/{total})
            </span>
        </div>
        {'<ul style="margin:4px 0 8px 0;padding-left:16px;list-style:none;">' + done_rows + pending_rows + '</ul>' if total else ''}
    </div>""")

    return "".join(cards) or '<p style="color:#aaa;font-size:13px;">No tasks today.</p>'


def meal_row(label: str, items: list) -> str:
    if not items:
        return ""
    return f"""
        <tr>
            <td style="padding:5px 12px 5px 0;color:#888;font-size:13px;white-space:nowrap;vertical-align:top;">{label}</td>
            <td style="padding:5px 0;font-size:14px;color:#222;">{"  ·  ".join(items)}</td>
        </tr>"""


def tomorrow_section(token: str, tomorrow: str) -> str:
    dt = datetime.strptime(tomorrow, "%Y-%m-%d")
    label = dt.strftime("%A, %B %-d")

    meals = fetch_meals(token, tomorrow)
    events = fetch_events(token, tomorrow)

    meal_rows = (
        meal_row("Breakfast", meals["Breakfast"]) +
        meal_row("Lunch",     meals["Lunch"]) +
        meal_row("Dinner",    meals["Dinner"]) +
        meal_row("Snack",     meals["Snack"])
    )
    has_meals = any(meals.values())

    event_rows = "".join(f"""
        <tr>
            <td style="padding:5px 12px 5px 0;color:#888;font-size:13px;white-space:nowrap;vertical-align:top;">{e['time']}</td>
            <td style="padding:5px 0;font-size:14px;color:#222;">{e['summary']}
                {"<br><span style='font-size:12px;color:#aaa;'>" + e['location'] + "</span>" if e['location'] else ""}
            </td>
        </tr>""" for e in events)

    blocks = ""
    if events:
        blocks += f"""
        <div style="margin-bottom:14px;">
            <div style="font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:#aaa;margin-bottom:8px;">Events</div>
            <table>{event_rows}</table>
        </div>"""
    if has_meals:
        blocks += f"""
        <div>
            <div style="font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:#aaa;margin-bottom:8px;">Meals</div>
            <table>{meal_rows}</table>
        </div>"""
    if not blocks:
        blocks = '<p style="color:#aaa;font-size:13px;">Nothing on the calendar yet.</p>'

    return f"""
    <div style="margin-bottom:28px;">
        <div style="font-size:13px;font-weight:700;text-transform:uppercase;
                    letter-spacing:1px;color:#888;margin-bottom:10px;">Tomorrow — {label}</div>
        {blocks}
    </div>"""


def build_html(day: str, chores: dict, token: str) -> str:
    dt = datetime.strptime(day, "%Y-%m-%d")
    day_label = dt.strftime("%A, %B %-d")
    tomorrow = (dt + timedelta(days=1)).strftime("%Y-%m-%d")

    chore_html = build_chore_summary(chores)
    tomorrow_html = tomorrow_section(token, tomorrow)

    return f"""
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"></head>
<body style="margin:0;padding:0;background:#f5f5f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;">
  <div style="max-width:540px;margin:32px auto;background:#fff;
              border-radius:8px;overflow:hidden;box-shadow:0 1px 4px rgba(0,0,0,0.08);">

    <!-- Header -->
    <div style="background:#222;padding:20px 24px;">
        <div style="font-size:11px;text-transform:uppercase;letter-spacing:2px;color:#888;">Evening Recap</div>
        <div style="font-size:22px;font-weight:700;color:#fff;margin-top:4px;">{day_label}</div>
    </div>

    <!-- Body -->
    <div style="padding:24px;">

        <!-- Chore recap -->
        <div style="margin-bottom:28px;">
            <div style="font-size:13px;font-weight:700;text-transform:uppercase;
                        letter-spacing:1px;color:#888;margin-bottom:14px;">Today's Chores</div>
            {chore_html}
        </div>

        <!-- Tomorrow preview -->
        {tomorrow_html}

    </div>

    <!-- Footer -->
    <div style="padding:14px 24px;background:#fafafa;border-top:1px solid #eee;
                font-size:11px;color:#bbb;text-align:center;">
        Hebert Five · Evening Recap · {day}
    </div>
  </div>
</body>
</html>"""


def send_email(html: str, day: str, gmail_password: str):
    dt = datetime.strptime(day, "%Y-%m-%d")
    subject = f"Hebert Five - Evening Recap — {dt.strftime('%A, %B %-d')}"

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
    parser = argparse.ArgumentParser(description="Send evening household recap email")
    parser.add_argument("--gmail-password", required=True, help="Gmail app password")
    parser.add_argument("--date", default=date.today().isoformat(), help="Date YYYY-MM-DD (default: today)")
    parser.add_argument("--preview", action="store_true", help="Print HTML instead of sending")
    args = parser.parse_args()

    token = load_token()

    print(f"Fetching data for {args.date}...")
    chores = fetch_chores(token, args.date)
    html = build_html(args.date, chores, token)

    if args.preview:
        print(html)
    else:
        print(f"Sending to {', '.join(TO_EMAILS)}...")
        send_email(html, args.date, args.gmail_password)
        print("Sent.")


if __name__ == "__main__":
    main()
