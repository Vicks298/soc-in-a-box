import json
import os


OUTPUT_DIR = "reports/output"


def export_json(report):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    path = f"{OUTPUT_DIR}/{report['incident_id']}.json"
    with open(path, "w") as f:
        json.dump(report, f, indent=2)

    return path


def export_markdown(report):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    path = f"{OUTPUT_DIR}/{report['incident_id']}.md"
    with open(path, "w") as f:
        f.write(f"# Incident Report {report['incident_id']}\n\n")
        f.write(f"**Severity:** {report['severity']}\n\n")
        f.write(f"**Source IP:** {report['source_ip']}\n\n")
        f.write(f"## Executive Summary\n")
        f.write(f"{report['executive_summary']}\n\n")

        f.write("## MITRE ATT&CK Mapping\n")
        f.write(
            f"- {report['mitre']['technique_id']} — "
            f"{report['mitre']['technique']}\n\n"
        )

        f.write("## Timeline\n")
        for e in report["timeline"]:
            f.write(f"- {e['timestamp']} — {e['activity']}\n")

        f.write("\n## Recommendation\n")
        f.write(report["recommendation"])

    return path
