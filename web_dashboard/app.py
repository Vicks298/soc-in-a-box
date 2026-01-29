from flask import Flask, render_template
import json
from collections import Counter

app = Flask(__name__)

CASE_STORE = "../case_management/case_store.json"


def load_cases():
    try:
        with open(CASE_STORE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


@app.route("/")
def dashboard():
    cases = load_cases()

    status_counts = Counter(c["status"] for c in cases)
    severity_counts = Counter(c["severity"] for c in cases)

    return render_template(
        "dashboard.html",
        total=len(cases),
        status=status_counts,
        severity=severity_counts,
        cases=cases[-10:]
    )


if __name__ == "__main__":
    app.run(debug=True)
