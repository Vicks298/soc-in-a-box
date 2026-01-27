from collections import defaultdict


def build_timeline(correlated_alerts):
    """
    Build chronological incident timelines from correlated alerts
    """
    incidents = []

    for alert in correlated_alerts:
        events = []

        for e in alert["events"]:
            events.append({
                "timestamp": e["timestamp"],
                "type": e.get("attack") or e.get("attack_type") or e.get("type"),
                "raw": e.get("raw", "")
            })

        events.sort(key=lambda x: x["timestamp"])

        incidents.append({
            "source_ip": alert["source_ip"],
            "attack": alert["attack"],
            "severity": alert["severity"],
            "timeline": events,
            "mitre": alert["mitre"]
        })

    return incidents
