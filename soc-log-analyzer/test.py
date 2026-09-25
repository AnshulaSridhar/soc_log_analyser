from log_parser import parse_logs
from detector import detect_bruteforce

df = parse_logs("data/auth.log")

findings = detect_bruteforce(df)

print(findings)