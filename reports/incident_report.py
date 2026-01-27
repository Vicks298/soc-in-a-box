import uuid
from datetime import datetime


def generate_incident_report(incident):
    """
    Generate SOC-style incident report
    """
    report = {
        "incident_id": f"INC-{uuid.uuid4().hex[:8].upper()}",
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "source_ip": incident["source_ip"],
        "attack": incident["attack"],
        "severity": incident["severity"],
        "mitre": incident["mitre"],
        "executive_summary": (
            f"A {incident['severity']} severity security incident was detected "
            f"originating from {incident['source_ip']} involving "
            f"{incident['attack']}."
        ),
        "timeline": [
            {
                "timestamp": e["timestamp"].isoformat(),
                "activity": e["type"]
            }
            for e in incident["timeline"]
        ],
        "recommendation": (
            "Review affected systems, reset compromised credentials, "
            "and block malicious IP addresses."
        )
    }

    return report
