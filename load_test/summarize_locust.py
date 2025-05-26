import csv

with open("locust_report_stats.csv") as f:
    reader = csv.DictReader(f)
    rows = [row for row in reader if row["Name"] not in ("Aggregated", "")]

print(rows)

md = "| Name | # Requests | Fails | Avg Resp Time (ms) | RPS |\n"
md += "|------|-------------|-------|--------------------|-----|\n"

for row in rows:
    md += f"| {row['Name']} | {row['# requests']} | {row['# failures']} | {row['Average response time']} | {row['Requests/s']} |\n"

with open("locust_summary.md", "w") as out:
    out.write(md)
