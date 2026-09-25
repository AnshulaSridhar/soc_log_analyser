import streamlit as st
import os


st.write("Current directory:", os.getcwd())
st.write("Files:", os.listdir("."))

if os.path.exists("data/auth.log"):
    st.success("auth.log FOUND")
else:
    st.error("auth.log NOT FOUND")
from log_parser import parse_logs
from detector import detect_events

df = parse_logs("data/auth.log")

findings = detect_events(df)

st.set_page_config(
    page_title="SOC Dashboard",
    layout="wide"
)

st.title("SOC Log Analyzer Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Alerts",
    len(findings)
)

col2.metric(
    "Critical Alerts",
    len(
        findings[
            findings["Severity"] == "CRITICAL"
        ]
    )
)

col3.metric(
    "High Alerts",
    len(
        findings[
            findings["Severity"] == "HIGH"
        ]
    )
)

col4.metric(
    "Unique Attackers",
    findings["IP"].nunique()
)

st.subheader("Security Findings")

st.dataframe(findings)

st.subheader("MITRE ATT&CK Mapping")

st.dataframe(
    findings[
        ["Attack", "MITRE"]
    ]
)

st.subheader("Top Attacking IPs")

st.bar_chart(
    df["ip"].value_counts()
)

st.subheader("Attack Distribution")

st.bar_chart(
    findings["Attack"].value_counts()
)

st.subheader("Severity Distribution")

st.bar_chart(
    findings["Severity"].value_counts()
)