from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(df):

    pdf = SimpleDocTemplate(
        "detections/incident_report.pdf"
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "SOC Incident Report",
            styles["Title"]
        )
    )

    for _, row in df.iterrows():

        content.append(
            Paragraph(
                str(row.to_dict()),
                styles["Normal"]
            )
        )

    pdf.build(content)