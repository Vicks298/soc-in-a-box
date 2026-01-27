def detect(events):
    alerts = []
    for e in events:
        if "Accepted password" in e["raw"]:
            alerts.append({
                "type": "Successful Login",
                "source_ip": e["raw"].split()[-1],
                "timestamp": e["timestamp"],
                "event": e
            })
    return alerts
