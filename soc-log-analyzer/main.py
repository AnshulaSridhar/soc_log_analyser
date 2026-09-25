from log_parser import parse_logs
from detector import detect_events
from report_generator import generate_report
from pdf_report import generate_pdf

df = parse_logs("data/auth.log")

findings = detect_events(df)

generate_report(findings)
generate_pdf(findings)

print("Reports generated successfully")