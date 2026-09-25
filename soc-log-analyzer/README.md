# SOC Log Analyzer Dashboard

screenshots/dashboard.png

## Overview

SOC Log Analyzer Dashboard is a cybersecurity monitoring and detection platform built using Python and Streamlit.

The project analyzes SSH authentication logs, detects suspicious activity using custom detection rules, maps alerts to MITRE ATT&CK techniques, assigns severity scores, and generates automated incident reports in CSV and PDF formats.

The solution simulates real-world Security Operations Center (SOC) workflows and demonstrates practical skills in:

- Log Analysis
- Detection Engineering
- Security Monitoring
- Incident Reporting
- Threat Detection
- Security Analytics

---

## Features

✅ SSH Log Parsing

✅ Brute Force Attack Detection

✅ Root Account Attack Detection

✅ Credential Stuffing Detection

✅ Severity Scoring

✅ MITRE ATT&CK Mapping

✅ CSV Incident Reports

✅ PDF Incident Reports

✅ Interactive Security Dashboard

✅ Security Event Visualization

✅ Threat Analytics

---

## Detection Rules

| Attack Type | Severity | MITRE ATT&CK |
|------------|----------|-------------|
| Brute Force | HIGH | T1110 |
| Root Account Attack | CRITICAL | T1078 |
| Credential Stuffing | HIGH | T1110 |

---

## Dashboard Metrics

The dashboard provides:

- Total Alerts
- Critical Alerts
- High Alerts
- Unique Attackers
- Security Findings
- MITRE ATT&CK Mapping
- Attack Distribution
- Severity Distribution
- Top Attacking IPs

---

# Dashboard Screenshots

## 1. SOC Dashboard Overview

screenshots/dashboard.png

### Description

This dashboard provides a high-level SOC view of detected threats.

Displayed metrics include:

- Total security alerts detected
- Critical alert count
- High severity alert count
- Number of unique attacking IP addresses
- Detailed findings table containing:
  - Attack Type
  - Severity
  - Risk Score
  - MITRE ATT&CK Technique

---

## 2. MITRE ATT&CK Mapping

screenshots/mitre_mapping.png

### Description

Detected security events are mapped to the MITRE ATT&CK framework.

Examples:

- T1110 - Brute Force
- T1078 - Valid Accounts / Account Abuse

This helps security analysts understand attacker tactics and techniques.

---

## 3. Top Attacking IPs

screenshots/top_attacking_ips.png

### Description

This visualization highlights the most active source IP addresses observed in authentication logs.

Benefits:

- Identify threat actors
- Detect brute-force activity
- Prioritize investigations
- Monitor attack trends

---

## 4. Attack Distribution

screenshots/attack_distribution.png

### Description

Shows the frequency of detected attack categories:

- Brute Force
- Credential Stuffing
- Root Account Attacks

This allows quick identification of the most common threats in the environment.

---

## 5. Severity Distribution

screenshots/severity_distribution.png

### Description

Displays alert counts grouped by severity level.

Severity categories include:

- HIGH
- CRITICAL

This visualization helps analysts assess overall risk exposure.

---

## Sample Security Findings

| IP Address | Attack Type | Severity | Score | MITRE |
|------------|------------|-----------|--------|--------|
| 192.168.1.10 | Brute Force | HIGH | 80 | T1110 |
| 172.16.0.5 | Brute 