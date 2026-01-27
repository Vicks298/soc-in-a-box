from datetime import datetime
import re

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

    for alert in correlated_alerts:
        print("\n🚨 CORRELATED ALERT 🚨")
        print(f"Source IP : {alert['source_ip']}")
        print(f"Attack   : {alert['attack']}")
        print(f"Severity : {alert['severity']}")
        print(f"MITRE    : {alert['mitre']['technique_id']} - {alert['mitre']['technique']}")





