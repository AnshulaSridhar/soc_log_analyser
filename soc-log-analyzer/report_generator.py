def generate_report(findings):

    findings.to_csv(
        "detections/incident_report.csv",
        index=False
    )

    print(
        "Incident report saved."
    )