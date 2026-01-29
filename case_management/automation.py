from datetime import datetime
from case_management.case import update_case_status, add_case_note


def automate_case(case):
    severity = case["severity"]

    if severity == "HIGH":
        update_case_status(case["case_id"], "ESCALATED")
        add_case_note(
            case["case_id"],
            "Automatically escalated due to HIGH severity."
        )

    elif severity == "MEDIUM":
        update_case_status(case["case_id"], "INVESTIGATING")
        add_case_note(
            case["case_id"],
            "Marked for analyst investigation."
        )

    elif severity == "LOW":
        update_case_status(case["case_id"], "CLOSED")
        add_case_note(
            case["case_id"],
            "Automatically closed due to LOW severity."
        )

    return case
