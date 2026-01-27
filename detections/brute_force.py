def detect(events):
    alerts = []
    for e in events:
        if "Failed password" in e["raw"]:
            alerts.append({
                "type": "SSH Brute Force",
                "source_ip": e["raw"].split()[-1],
                "timestamp": e["timestamp"],
                "event": e
            })
    return alerts
