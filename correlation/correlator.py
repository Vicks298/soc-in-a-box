from collections import defaultdict
from mitre.attack_mapping import map_attack_to_mitre


def get_attack_name(alert):
    """
    Safely extract attack name from detection output
    """
    return (
        alert.get("attack")
        or alert.get("attack_type")
        or alert.get("type")
        or "Unknown"
    )


def correlate(alerts):
    grouped = defaultdict(list)

    # Group alerts by source IP
    for alert in alerts:
        grouped[alert["source_ip"]].append(alert)

    correlated_alerts = []

    for source_ip, alert_group in grouped.items():
        attack_names = [get_attack_name(a) for a in alert_group]

        # Correlation logic
        if "SSH Brute Force" in attack_names and "Successful Login" in attack_names:
            attack = "Successful Login After Brute Force"
            severity = "HIGH"
        elif "SSH Brute Force" in attack_names:
            attack = "SSH Brute Force"
            severity = "MEDIUM"
        elif "Suspicious Web Activity" in attack_names:
            attack = "Suspicious Web Activity"
            severity = "MEDIUM"
        else:
            attack = "Suspicious Activity"
            severity = "LOW"

        correlated_alerts.append({
            "source_ip": source_ip,
            "attack": attack,
            "severity": severity,
            "mitre": map_attack_to_mitre(attack),
            "events": alert_group
        })

    return correlated_alerts



