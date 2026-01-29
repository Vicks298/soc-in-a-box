from datetime import datetime

# -------------------------
# Detections
# -------------------------
from detections.brute_force import detect as detect_bruteforce
from detections.successful_login import detect as detect_login
from detections.web_access import detect as detect_web

# -------------------------
# Correlation + DFIR
# -------------------------
from correlation.correlator import correlate
from dfir.timeline import build_timeline

# -------------------------
# Reports & Export
# -------------------------
from reports.incident_report import generate_incident_report
from reports.exporter import export_json, export_markdown

# -------------------------
# Case Management + Automation
# -------------------------
from case_management.case import create_case
from case_management.automation import automate_case
from dashboard.soc_dashboard import render_dashboard


# -------------------------
# Log sources
# -------------------------
LOG_FILES = {
    "auth": "logs/auth.log",
    "web": "logs/web.log",
    "firewall": "logs/firewall.log"
}


# -------------------------
# Parsing
# -------------------------
def parse_event(source, line):
    return {
        "timestamp": datetime.strptime(line[:15], "%b %d %H:%M:%S"),
        "source": source,
        "raw": line.strip()
    }


def ingest_logs():
    events = []

    for source, path in LOG_FILES.items():
        with open(path, "r") as f:
            for line in f:
                events.append(parse_event(source, line))

    return sorted(events, key=lambda x: x["timestamp"])


# -------------------------
# MAIN PIPELINE
# -------------------------
if __name__ == "__main__":

    # STEP 1 — Ingestion
    events = ingest_logs()
    print(f"[STEP 1] Events ingested: {len(events)}")

    # STEP 2 — Detections
    alerts = []
    alerts += detect_bruteforce(events)
    alerts += detect_login(events)
    alerts += detect_web(events)
    print(f"[STEP 2] Raw alerts generated: {len(alerts)}")

    # STEP 3 — Correlation
    correlated_alerts = correlate(alerts)
    print(f"[STEP 3] Correlated incidents: {len(correlated_alerts)}")

    # STEP 4 — DFIR Timeline
    incidents = build_timeline(correlated_alerts)
    print(f"[STEP 4] Incidents with timelines built: {len(incidents)}")

    # STEP 5–8 — Reports, Export, Case Mgmt, Automation
    for incident in incidents:
        report = generate_incident_report(incident)

        json_path = export_json(report)
        md_path = export_markdown(report)

        case = create_case(report)
        automate_case(case)

        print("\n🚨 SOC INCIDENT 🚨")
        print(f"Incident ID : {report['incident_id']}")
        print(f"Case ID     : {case['case_id']}")
        print(f"Severity    : {report['severity']}")
        print(f"Status      : {case['status']}")
        print(f"Summary     : {report['executive_summary']}")
        print(f"JSON Report : {json_path}")
        print(f"MD Report   : {md_path}")

        # STEP 9 — SOC Dashboard (CLI)
    render_dashboard()







