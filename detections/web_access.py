def detect(events):
    alerts = []
    for e in events:
        if "/admin" in e["raw"] or "/upload" in e["raw"]:
            alerts.append({
                "type": "Suspicious Web Access",
                "source_ip": e["raw"].split()[-1],
                "timestamp": e["timestamp"],
                "event": e
            })
    return alerts
