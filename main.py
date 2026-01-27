from datetime import datetime
import re

from dfir.timeline import build_timeline
from detections.brute_force import detect as detect_bruteforce
from detections.successful_login import detect as detect_login
from detections.web_access import detect as detect_web
from correlation.correlator import correlate

LOG_FILES = {
    "auth": "logs/auth.log",
    "web": "logs/web.log",
    "firewall": "logs/firewall.log"
}


def extract_ip(line):
    match = re.search(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", line)
    return match.group(0) if match else "unknown"


def parse_event(source, line):
    return {
        "timestamp": datetime.strptime(line[:15], "%b %d %H:%M:%S"),
        "source": source,
        "raw": line.strip(),
        "source_ip": extract_ip(line)
    }


def ingest_logs():
    events = []
    for source, path in LOG_FILES.items():
        try:
            with open(path) as f:
                for line in f:
                    events.append(parse_event(source, line))
        except FileNotFoundError:
            print(f"[!] Missing log file: {path}")

    return events


if __name__ == "__main__":
    events = ingest_logs()

    alerts = []
    alerts.extend(detect_bruteforce(events))
    alerts.extend(detect_login(events))
    alerts.extend(detect_web(events))

    correlated_alerts = correlate(alerts)

    incidents = build_timeline(correlated_alerts)

for incident in incidents:
    print("\n🧠 INCIDENT TIMELINE 🧠")
    print(f"Source IP: {incident['source_ip']}")
    print(f"Attack: {incident['attack']}")
    print(f"Severity: {incident['severity']}")
    print(f"MITRE: {incident['mitre']['technique_id']} - {incident['mitre']['technique']}")

    for e in incident["timeline"]:
        print(f"[{e['timestamp']}] {e['type']}")





