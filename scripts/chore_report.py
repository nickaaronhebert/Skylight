#!/usr/bin/env python3
"""
Chore completion report for a given user and date range.

Usage:
  python3 scripts/chore_report.py --user Eleanor --start 2026-05-01 --end 2026-05-31 --token <bearer_token>

Users: Eleanor, Delaney, Marley, Elizabeth, "Evening Assistant", Family
"""

import argparse
import json
import sys
import urllib.request
from datetime import datetime

FRAME_ID = "5289925"
BASE_URL = "https://app.ourskylight.com"

CATEGORY_IDS = {
    "eleanor":          "20235057",
    "delaney":          "20235070",
    "marley":           "20235082",
    "elizabeth":        "20235149",
    "evening assistant": "20237876",
    "family":           "20235749",
}


def fetch_chores(token: str, start: str, end: str) -> list:
    url = (
        f"{BASE_URL}/api/frames/{FRAME_ID}/chores"
        f"?after={start}&before={end}&include_late=true"
    )
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "skylight-api-version": "2026-04-15",
        "User-Agent": "Mozilla/5.0",
    })
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())["data"]


def build_report(chores: list, category_id: str) -> dict:
    user_chores = [
        c for c in chores
        if c["relationships"]["category"]["data"]
        and c["relationships"]["category"]["data"]["id"] == category_id
    ]

    total = len(user_chores)
    completed = [c for c in user_chores if c["attributes"]["status"] == "complete"]
    pending = [c for c in user_chores if c["attributes"]["status"] != "complete"]
    pct = (len(completed) / total * 100) if total > 0 else 0

    return {
        "total": total,
        "completed": len(completed),
        "pending": len(pending),
        "completion_rate": round(pct, 1),
        "completed_tasks": [c["attributes"]["summary"] for c in completed],
        "pending_tasks": [c["attributes"]["summary"] for c in pending],
    }


def print_report(user: str, start: str, end: str, report: dict):
    bar_filled = int(report["completion_rate"] / 5)
    bar = "█" * bar_filled + "░" * (20 - bar_filled)

    print(f"\n{'═' * 50}")
    print(f"  Chore Report — {user.title()}")
    print(f"  {start} → {end}")
    print(f"{'═' * 50}")
    print(f"  [{bar}] {report['completion_rate']}%")
    print(f"  {report['completed']} of {report['total']} tasks completed")
    print()

    if report["completed_tasks"]:
        print("  ✓ Completed")
        for t in report["completed_tasks"]:
            print(f"    · {t}")
        print()

    if report["pending_tasks"]:
        print("  ✗ Not completed")
        for t in report["pending_tasks"]:
            print(f"    · {t}")
        print()

    print(f"{'═' * 50}\n")


def main():
    parser = argparse.ArgumentParser(description="Skylight chore completion report")
    parser.add_argument("--user", required=True, help="User name (e.g. Eleanor)")
    parser.add_argument("--start", required=True, help="Start date YYYY-MM-DD")
    parser.add_argument("--end", required=True, help="End date YYYY-MM-DD")
    parser.add_argument("--token", required=True, help="Bearer token")
    parser.add_argument("--json", action="store_true", help="Output raw JSON instead of formatted report")
    args = parser.parse_args()

    category_id = CATEGORY_IDS.get(args.user.lower())
    if not category_id:
        print(f"Unknown user '{args.user}'. Valid options: {', '.join(CATEGORY_IDS.keys())}", file=sys.stderr)
        sys.exit(1)

    try:
        datetime.strptime(args.start, "%Y-%m-%d")
        datetime.strptime(args.end, "%Y-%m-%d")
    except ValueError:
        print("Dates must be in YYYY-MM-DD format.", file=sys.stderr)
        sys.exit(1)

    chores = fetch_chores(args.token, args.start, args.end)
    report = build_report(chores, category_id)

    if args.json:
        print(json.dumps({"user": args.user, "start": args.start, "end": args.end, **report}, indent=2))
    else:
        print_report(args.user, args.start, args.end, report)


if __name__ == "__main__":
    main()
