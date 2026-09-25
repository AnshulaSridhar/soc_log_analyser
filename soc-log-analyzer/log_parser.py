import re
import pandas as pd

def parse_logs(file_path):

    records = []

    with open(file_path, "r") as file:

        for line in file:

            ip_match = re.search(
                r'(\d+\.\d+\.\d+\.\d+)',
                line
            )

            if ip_match:

                records.append({
                    "log": line.strip(),
                    "ip": ip_match.group()
                })

    return pd.DataFrame(records)