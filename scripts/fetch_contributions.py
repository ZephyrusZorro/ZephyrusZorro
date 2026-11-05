#!/usr/bin/env python3
"""
Scrapes real daily contribution counts from GitHub's public endpoint
(the unauthenticated HTML fragment used by profile calendars)
and writes data/contributions.json with streak statistics and monthly totals.

Includes fallback to github-contributions API for maximum resilience.
Zero mandatory external dependencies (uses urllib + re with optional requests/bs4).
"""
import datetime
import json
import os
import re
import sys
import urllib.request

USERNAME = os.environ.get("GH_PROFILE_USER", "ZephyrusZorro")
HTML_URL = f"https://github.com/users/{USERNAME}/contributions"
API_URL = f"https://github-contributions-api.jogruber.de/v4/{USERNAME}?y=last"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT_PATH = os.path.join(HERE, "..", "data", "contributions.json")


def fetch_from_github_html():
    req = urllib.request.Request(
        HTML_URL,
        headers={"User-Agent": "Mozilla/5.0 (compatible; ZephyrusZorroProfileBot/1.0)"}
    )
    with urllib.request.urlopen(req, timeout=25) as resp:
        content = resp.read().decode("utf-8")

    tooltips = dict(re.findall(r'<tool-tip[^>]*for="([^"]+)"[^>]*>(.*?)</tool-tip>', content, re.DOTALL))
    cells = re.findall(r'<td[^>]*class="[^"]*ContributionCalendar-day[^"]*"[^>]*>', content)

    if not cells:
        return None

    days = []
    for cell in cells:
        m_date = re.search(r'data-date="([^"]+)"', cell)
        m_id = re.search(r'id="([^"]+)"', cell)
        m_lvl = re.search(r'data-level="([^"]+)"', cell)
        if not m_date:
            continue
        date = m_date.group(1)
        cell_id = m_id.group(1) if m_id else ""
        lvl = int(m_lvl.group(1)) if m_lvl else 0
        txt = tooltips.get(cell_id, "")
        if "no contributions" in txt.lower():
            cnt = 0
        else:
            m_cnt = re.search(r"(\d+)", txt)
            cnt = int(m_cnt.group(1)) if m_cnt else 0
        days.append({"date": date, "count": cnt, "level": lvl})

    days.sort(key=lambda d: d["date"])
    return days


def fetch_from_fallback_api():
    req = urllib.request.Request(API_URL, headers={"User-Agent": "ZephyrusZorroProfileBot/1.0"})
    with urllib.request.urlopen(req, timeout=25) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    contribs = data.get("contributions", [])
    days = []
    for c in contribs:
        days.append({
            "date": c["date"],
            "count": c.get("count", 0),
            "level": c.get("level", 0)
        })
    days.sort(key=lambda d: d["date"])
    return days


def compute_current_streak(days):
    if not days:
        return 0, None, None
    idx = len(days) - 1
    # If today hasn't ended and has 0 commits, check from yesterday so streak isn't wiped mid-day
    if days[idx]["count"] == 0 and idx > 0:
        idx -= 1
    streak = 0
    end_idx = idx
    while idx >= 0 and days[idx]["count"] > 0:
        streak += 1
        idx -= 1
    start_idx = idx + 1
    if streak == 0:
        return 0, None, None
    return streak, days[start_idx]["date"], days[end_idx]["date"]


def compute_longest_streak(days):
    longest = run = 0
    longest_start = longest_end = None
    run_start_idx = None
    for i, d in enumerate(days):
        if d["count"] > 0:
            if run == 0:
                run_start_idx = i
            run += 1
            if run > longest:
                longest = run
                longest_start = days[run_start_idx]["date"]
                longest_end = days[i]["date"]
        else:
            run = 0
    return longest, longest_start, longest_end


def build_data(days):
    total = sum(d["count"] for d in days)
    active_days = sum(1 for d in days if d["count"] > 0)
    best = max(days, key=lambda d: d["count"]) if days else {"date": "N/A", "count": 0}
    cur_len, cur_start, cur_end = compute_current_streak(days)
    long_len, long_start, long_end = compute_longest_streak(days)

    monthly = {}
    for d in days:
        key = d["date"][:7]
        monthly[key] = monthly.get(key, 0) + d["count"]
    monthly_list = [{"month": k, "total": v} for k, v in sorted(monthly.items())]

    return {
        "username": USERNAME,
        "generated_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "range": {"start": days[0]["date"] if days else "N/A", "end": days[-1]["date"] if days else "N/A"},
        "total_contributions": total,
        "active_days": active_days,
        "avg_per_active_day": round(total / active_days, 1) if active_days else 0,
        "current_streak": {"length": cur_len, "start": cur_start, "end": cur_end},
        "longest_streak": {"length": long_len, "start": long_start, "end": long_end},
        "best_day": {"date": best["date"], "count": best["count"]},
        "monthly": monthly_list,
        "days": days,
    }


def main():
    print(f"Fetching contribution data for @{USERNAME}...")
    days = None
    try:
        days = fetch_from_github_html()
        if days:
            print(f"Successfully scraped {len(days)} calendar days from GitHub HTML.")
    except Exception as e:
        print(f"HTML scraper notice: {e}, attempting API fallback...", file=sys.stderr)

    if not days:
        try:
            days = fetch_from_fallback_api()
            print(f"Successfully fetched {len(days)} days from fallback API.")
        except Exception as e:
            print(f"Fallback API failed: {e}", file=sys.stderr)
            sys.exit(1)

    data = build_data(days)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Wrote {OUT_PATH}: {data['total_contributions']} contributions, "
          f"Current streak: {data['current_streak']['length']}d, "
          f"Longest streak: {data['longest_streak']['length']}d")


if __name__ == "__main__":
    main()
