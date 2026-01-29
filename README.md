# 🛡️ SOC-in-a-Box

SOC-in-a-Box is a hands-on security engineering project that simulates how a real Security Operations Center (SOC) detects, correlates, investigates, and manages security incidents.

This project was built incrementally (step-by-step) to reflect how SOC platforms evolve in real environments.

---

## 📌 What This Project Does

SOC-in-a-Box takes raw log data and turns it into actionable security incidents by:

1. Ingesting logs
2. Running detection logic
3. Correlating alerts
4. Building incident timelines (DFIR)
5. Managing cases
6. Displaying SOC dashboards

---

## 🧠 Core Capabilities Implemented

### ✅ Log Ingestion

* Parses authentication, web, and firewall logs
* Normalizes events into a common structure

### ✅ Detection Engineering

* Brute-force login detection
* Suspicious successful login detection
* Web access anomaly detection

### ✅ Alert Correlation

* Groups related alerts into a single incident
* Reduces alert noise
* Produces higher-confidence incidents

### ✅ DFIR Timeline Reconstruction

* Orders events chronologically
* Helps analysts understand attack progression

### ✅ MITRE ATT&CK Mapping

* Maps detected activity to MITRE ATT&CK techniques
* Adds threat context to incidents

### ✅ Case Management

* Automatic case creation
* Case lifecycle tracking (OPEN, INVESTIGATING, ESCALATED, CLOSED)

### ✅ Case Lifecycle Automation (SOAR-style)

* HIGH severity → Escalated automatically
* MEDIUM severity → Marked for investigation
* LOW severity → Auto-closed

---

## 📊 SOC Dashboards

### 🖥️ CLI Dashboard (Primary)

Used like an internal SOC tool:

* Case counts
* Severity breakdown
* Status overview
* Recent incidents

Run:

```bash
python dashboard/soc_dashboard.py
```

### 🌐 Web Dashboard (Viewer-Only)

Read-only dashboard for demonstration purposes.

* Displays case statistics
* Does not modify data

Run:

```bash
cd web_dashboard
python app.py
```

---

## ▶️ How to Run the Full SOC Pipeline

```bash
python main.py
```

This runs:

* Log ingestion
* Detections
* Correlation
* DFIR timeline building
* Case creation
* Automation
* Dashboard output

---

## 📂 Project Structure (Simplified)

```
SOC-in-a-Box/
├── detections/
├── correlation/
├── mitre/
├── case_management/
├── dashboard/
├── web_dashboard/
├── logs/
├── main.py
└── README.md
```

---

## 🚧 Future Enhancements (Planned)

The following components are intentionally designed but not fully implemented yet:

* Risk scoring engine
* Automated response actions
* External threat intelligence ingestion
* Hosted web dashboard (Render-ready)

These represent realistic SOC platform growth phases.

---

## 🎯 What This Project Demonstrates

* SOC analyst workflows
* Detection engineering mindset
* Incident response and DFIR thinking
* Alert correlation and noise reduction
* Case lifecycle management

---

## ⚠️ Disclaimer

This project is for educational and portfolio demonstration purposes only.
It is not intended for production use.
