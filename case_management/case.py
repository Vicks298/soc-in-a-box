import json
import os
from datetime import datetime
import uuid

CASE_STORE = "case_management/case_store.json"


def load_cases():
    if not os.path.exists(CASE_STORE):
        return []
    with open(CASE_STORE, "r") as f:
        return json.load(f)


def save_cases(cases):
    with open(CASE_STORE, "w") as f:
        json.dump(cases, f, indent=2)


def create_case(report):
    cases = load_cases()

    case = {
        "case_id": f"CASE-{uuid.uuid4().hex[:6].upper()}",
        "incident_id": report["incident_id"],
        "status": "OPEN",
        "severity": report["severity"],
        "assigned_to": "SOC-Analyst-1",
        "created_at": datetime.utcnow().isoformat() + "Z",
        "updated_at": datetime.utcnow().isoformat() + "Z",
        "summary": report["executive_summary"],
        "timeline": report["timeline"],
        "notes": [],
        "evidence": {
            "source_ip": report["source_ip"],
            "mitre": report["mitre"]
        }
    }

    cases.append(case)
    save_cases(cases)

    return case


def update_case_status(case_id, new_status):
    cases = load_cases()

    for case in cases:
        if case["case_id"] == case_id:
            case["status"] = new_status
            case["updated_at"] = datetime.utcnow().isoformat() + "Z"
            save_cases(cases)
            return case

    return None


def add_case_note(case_id, note):
    cases = load_cases()

    for case in cases:
        if case["case_id"] == case_id:
            case["notes"].append({
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "note": note
            })
            case["updated_at"] = datetime.utcnow().isoformat() + "Z"
            save_cases(cases)
            return case

    return None
