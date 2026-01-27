import json


def load_intel():
    with open("threat_intel/intel.json") as f:
        return json.load(f)["indicators"]


def enrich_with_intel(alert):
    intel = load_intel()

    for indicator in intel:
        if indicator["value"] == alert["source_ip"]:
            alert["threat_intel"] = indicator
            alert["intel_match"] = True
            return alert

    alert["intel_match"] = False
    return alert
