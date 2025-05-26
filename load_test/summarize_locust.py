import csv

with open("locust_report_stats.csv") as f:
    reader = csv.DictReader(f)
    rows = [row for row in reader if row["Name"] not in ("Aggregated", "")]

print(rows)

md = "| Name | # Requests | Min (ms) | 50% (ms) | 90% (ms) | 99% (ms) | Max (ms) | # Fails | RPS |\n"
md += "|------|------------|----------|----------|----------|----------|----------|-------|-----|\n"

for row in rows:
    md += f"| {row['Name']} | {row['Request Count']} | {row['Min Response Time']} | {row['50%']} | {row['90%']} | {row['99%']} | {row['Max Response Time']} | {row['Failure Count']} | {row['Requests/s'][:5]} |\n"

with open("locust_summary.md", "w") as out:
    out.write(md)