import os
import streamlit as st

from log_parser import parse_logs
from detector import detect_events

# --------------------------------------------------
# File Path Fix (Works Locally + Streamlit Cloud)
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_PATH = os.path.join(
    BASE_DIR,
    "data",
    "auth.log"
)

# --------------------------------------------------
# Load Data
# --------------------------------------------------

df = parse_logs(LOG_PATH)

findings = detect_events(df)

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="SOC Log Analyzer Dashboard",
    layout="wide"
)

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("SOC Log Analyzer Dashboard")

st.markdown(
    """
    Detects malicious login activity from SSH authentication logs
    using custom cybersecurity detection rules.
    """
)

# --------------------------------------------------
# Metrics
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Alerts",
        len(findings)
    )

with col2:
    st.metric(
        "Critical Alerts",
        len(
            findings[
                findings["Severity"] == "CRITICAL"
            ]
        )
    )

with col3:
    st.metric(
        "High Alerts",
        len(
            findings[
                findings["Severity"] == "HIGH"
            ]
        )
    )

with col4:
    st.metric(
        "Unique Attackers",
        findings["IP"].nunique()
    )

# --------------------------------------------------
# Security Findings
# --------------------------------------------------

st.subheader("Security Findings")

st.dataframe(
    findings,
    use_container_width=True
)

# --------------------------------------------------
# MITRE ATT&CK Mapping
# --------------------------------------------------

st.subheader("MITRE ATT&CK Mapping")

st.dataframe(
    findings[
        ["Attack", "MITRE"]
    ].drop_duplicates(),
    use_container_width=True
)

# --------------------------------------------------
# Top Attacking IPs
# --------------------------------------------------

st.subheader("Top Attacking IPs")

st.bar_chart(
    df["ip"].value_counts()
)

# --------------------------------------------------
# Attack Distribution
# --------------------------------------------------

st.subheader("Attack Distribution")

st.bar_chart(
    findings["Attack"].value_counts()
)

# --------------------------------------------------
# Severity Distribution
# --------------------------------------------------

st.subheader("Severity Distribution")

st.bar_chart(
    findings["Severity"].value_counts()
)

# --------------------------------------------------
# Parsed Logs
# --------------------------------------------------

with st.expander("View Parsed Log Data"):
    st.dataframe(
        df,
        use_container_width=True
    )

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("---")

st.caption(
    "SOC Log Analyzer | Python | Streamlit | MITRE ATT&CK"
)