import json
from collections import Counter
from datetime import datetime

CASE_STORE = "case_management/case_store.json"


def load_cases():
    try:
        with open(CASE_STORE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def render_dashboard():
    cases = load_cases()

    total = len(cases)
    status_counts = Counter(c["status"] for c in cases)
    severity_counts = Counter(c["severity"] for c in cases)

    print("\n" + "=" * 45)
    print("🛡️  SOC-IN-A-BOX — DASHBOARD")
    print("=" * 45)
    print(f"Snapshot Time : {datetime.utcnow().isoformat()}Z\n")

    print(f"📁 Total Cases        : {total}")
    print(f"🟢 Open               : {status_counts.get('OPEN', 0)}")
    print(f"🟡 Investigating      : {status_counts.get('INVESTIGATING', 0)}")
    print(f"🔴 Escalated          : {status_counts.get('ESCALATED', 0)}")
    print(f"⚫ Closed             : {status_counts.get('CLOSED', 0)}")

    print("\n🔥 Severity Breakdown")
    print("-" * 30)
    print(f"HIGH   : {severity_counts.get('HIGH', 0)}")
    print(f"MEDIUM : {severity_counts.get('MEDIUM', 0)}")
    print(f"LOW    : {severity_counts.get('LOW', 0)}")

    print("\n🕒 Latest Cases")
    print("-" * 30)

    for case in cases[-5:]:
        print(
            f"{case['case_id']} | "
            f"{case['severity']} | "
            f"{case['status']} | "
            f"{case['created_at']}"
        )

    print("\n" + "=" * 45)
