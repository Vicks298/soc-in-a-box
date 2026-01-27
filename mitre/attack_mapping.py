MITRE_ATTACK_MAPPING = {
    "SSH Brute Force": {
        "tactic": "Credential Access",
        "technique": "Brute Force",
        "technique_id": "T1110"
    },
    "Successful Login After Brute Force": {
        "tactic": "Initial Access",
        "technique": "Valid Accounts",
        "technique_id": "T1078"
    },
    "Suspicious Web Activity": {
        "tactic": "Persistence",
        "technique": "Web Shell",
        "technique_id": "T1505"
    }
}


def map_attack_to_mitre(attack):
    return MITRE_ATTACK_MAPPING.get(
        attack,
        {
            "tactic": "Unknown",
            "technique": "Unknown",
            "technique_id": "N/A"
        }
    )


