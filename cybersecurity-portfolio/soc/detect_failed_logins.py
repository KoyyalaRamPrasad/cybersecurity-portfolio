
import csv
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

import sys
DATA_FILE = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent / "data" / "login_events.csv"
FAILURE_THRESHOLD = 5
TIME_WINDOW_MINUTES = 5

failed_events = defaultdict(list)

with DATA_FILE.open(newline="", encoding="utf-8") as file:
    while True:
        first_line = file.readline()
        if not first_line:
            break
        if first_line.strip() and not first_line.lstrip().startswith("#"):
            break

    reader = csv.DictReader(
        [first_line] + list(file)
    )

    for row in reader:
        if row["event_type"].strip().lower() != "login":
            continue

        if row["status"].strip().lower() != "failure":
            continue

        timestamp = datetime.fromisoformat(row["timestamp"])
        source_ip = row["source_ip"].strip()

        failed_events[source_ip].append(timestamp)

print("SOC Detection: Repeated Failed Logins")
print(f"Rule: {FAILURE_THRESHOLD}+ failures within "
      f"{TIME_WINDOW_MINUTES} minutes from one source IP")
print("Dataset: Simulated training data")
print("-" * 55)

alerts_found = False
window = timedelta(minutes=TIME_WINDOW_MINUTES)

for source_ip, timestamps in sorted(failed_events.items()):
    timestamps.sort()

    for start_index, start_time in enumerate(timestamps):
        end_index = start_index

        while (
            end_index + 1 < len(timestamps)
            and timestamps[end_index + 1] - start_time <= window
        ):
            end_index += 1

        count = end_index - start_index + 1

        if count >= FAILURE_THRESHOLD:
            print(
                f"ALERT: {source_ip} had {count} failed logins "
                f"within {TIME_WINDOW_MINUTES} minutes."
            )
            alerts_found = True
            break

if not alerts_found:
    print("No repeated-failed-login alerts detected.")
