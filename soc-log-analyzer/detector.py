import pandas as pd

def detect_events(df):

    alerts = []

    ip_counts = df["ip"].value_counts()

    for ip, count in ip_counts.items():

        if count >= 5:

            alerts.append({
                "IP": ip,
                "Attack": "Brute Force",
                "Severity": "HIGH",
                "Score": 80,
                "MITRE": "T1110"
            })

    root_logs = df[
        df["log"].str.contains(
            "Failed password for root",
            case=False
        )
    ]

    for ip in root_logs["ip"].unique():

        alerts.append({
            "IP": ip,
            "Attack": "Root Account Attack",
            "Severity": "CRITICAL",
            "Score": 100,
            "MITRE": "T1078"
        })

    usernames = {}

    for _, row in df.iterrows():

        line = row["log"]
        ip = row["ip"]

        try:

            if "Failed password for" in line:

                username = (
                    line.split("for")[1]
                    .split("from")[0]
                    .strip()
                )

                if ip not in usernames:
                    usernames[ip] = set()

                usernames[ip].add(username)

        except:
            pass

    for ip, users in usernames.items():

        if len(users) >= 3:

            alerts.append({
                "IP": ip,
                "Attack": "Credential Stuffing",
                "Severity": "HIGH",
                "Score": 90,
                "MITRE": "T1110"
            })

    return pd.DataFrame(alerts)