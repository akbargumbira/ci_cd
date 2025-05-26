import csv

with open("locust_report_stats.csv") as f:
    reader = csv.DictReader(f)
    rows = [row for row in reader if row["Name"] not in ("Aggregated", "")]

print(rows)

md = "| Name |  RPS | # Requests | # Fails | Min (ms) | 50% (ms) | 90% (ms) | 99% (ms) | Max (ms) |\n"
md += "|------|------------|----------|----------|----------|----------|----------|-------|-----|\n"

for row in rows:
    md += f"| {row['Name']} | {row['Requests/s'][:5]} | {row['Request Count']} | {row['Failure Count']} |{round(float(row['Min Response Time']), 2)} | {round(float(row['50%']), 2)} | {round(float(row['90%']), 2)} | {round(float(row['99%']), 2)} | {round(float(row['Max Response Time']), 2)} | \n"

with open("locust_summary.md", "w") as out:
    out.write(md)