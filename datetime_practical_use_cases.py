# ============================================================
# Practical use cases: Using datetime in DevOps
# ============================================================

# Practical DevOps examples with Python datetime module

from datetime import datetime, timedelta, timezone
import time


# 1. datetime.now()
# Practical use case: Add a timestamp when writing logs
current_time = datetime.now()
print("Current timestamp:", current_time)
# 👉 Why useful:
# When automating deployments or monitoring, you often add timestamps to logs
# so that events can be correlated later.
# ============================================================

# 2. datetime.utcnow()
# Practical use case: Generate UTC timestamps for distributed systems
utc_time = datetime.utcnow()
print("UTC time:", utc_time)
# 👉 Why useful:
# In multi-region setups (AWS, Azure, GCP), using UTC avoids timezone confusion in logs.
# ============================================================

# 3. datetime.fromtimestamp()
# Practical use case: Convert Unix epoch (log timestamp) to readable format
epoch = 1694275200  # Example: log entry timestamp
readable = datetime.fromtimestamp(epoch)
print("Converted from epoch:", readable)
# 👉 Why useful:
# Many tools (Docker, Kubernetes) output timestamps in epoch format. This makes them human-readable.
# ============================================================

# 4. datetime.timestamp()
# Practical use case: Store event times as epoch for compact logging
ts = current_time.timestamp()
print("Epoch timestamp:", ts)
# 👉 Why useful:
# Epoch timestamps are lightweight and language-agnostic. Useful when exporting logs to ELK, Prometheus, or CloudWatch.
# ============================================================

# 5. datetime.strftime()
# Practical use case: Format datetime for reports and filenames
formatted = current_time.strftime("%Y-%m-%d_%H-%M-%S")
print("Formatted timestamp for file:", formatted)
# 👉 Why useful:
# Great for naming backup files: e.g., db_backup_2025-09-09_13-00-00.sql
# ============================================================

# 6. datetime.strptime()
# Practical use case: Parse a timestamp string from logs
log_entry = "2025-09-09 13:45:00"
parsed = datetime.strptime(log_entry, "%Y-%m-%d %H:%M:%S")
print("Parsed datetime:", parsed)
# 👉 Why useful:
# Log files often contain date strings. Parsing lets you calculate durations or filter by time.
# ============================================================

# 7. timedelta
# Practical use case: Calculate SLA deadline (24h after ticket creation)
ticket_created = datetime.now()
sla_deadline = ticket_created + timedelta(hours=24)
print("SLA deadline:", sla_deadline)
# 👉 Why useful:
# In monitoring/alerting, you need to calculate deadlines and expiry times.
# ============================================================

# 8. datetime.replace()
# Practical use case: Normalize times (set seconds/microseconds to zero)
normalized = current_time.replace(second=0, microsecond=0)
print("Normalized datetime:", normalized)
# 👉 Why useful:
# Useful when aggregating metrics per minute/hour without microsecond noise.
# ============================================================

# 9. datetime.weekday()
# Practical use case: Run job only on weekdays
if current_time.weekday() < 5:
    print("Running weekday job")
# 👉 Why useful:
# Automations like backups or reports may be skipped on weekends.
# ============================================================

# 10. datetime.isoformat()
# Practical use case: Store timestamps in ISO 8601 for APIs
iso_str = current_time.isoformat()
print("ISO 8601 string:", iso_str)
# 👉 Why useful:
# ISO 8601 is the standard for exchanging timestamps between services (Kubernetes, APIs, JSON logs).
# ============================================================

# 11. datetime.combine()
# Practical use case: Combine a date and a fixed time (e.g., maintenance at 2 AM)
maintenance_date = datetime.today().date()
maintenance_time = datetime.strptime("02:00:00", "%H:%M:%S").time()
maintenance_dt = datetime.combine(maintenance_date, maintenance_time)
print("Planned maintenance:", maintenance_dt)
# 👉 Why useful:
# Scheduling recurring jobs (like database maintenance) often needs combining date and time.
# ============================================================

# 12. datetime.astimezone()
# Practical use case: Convert UTC logs into local timezone
utc_dt = datetime.now(timezone.utc)
local_dt = utc_dt.astimezone()
print("Local time:", local_dt)
# 👉 Why useful:
# DevOps often debug issues across timezones. Converting makes logs easier to understand.
# ============================================================

# 13. time.sleep() with datetime
# Practical use case: Delay retry with exponential backoff
for i in range(3):
    print(f"Attempt {i+1} at:", datetime.now())
    time.sleep(2 ** i)  # 1s, 2s, 4s
# 👉 Why useful:
# Retrying failed connections (DB, API) with backoff prevents overwhelming systems.
# ============================================================

# 14. Measuring durations
# Practical use case: Measure deployment step duration
start = datetime.now()
time.sleep(2)  # Simulate deployment step
end = datetime.now()
print("Deployment step took:", end - start)
# 👉 Why useful:
# Tracking durations helps identify bottlenecks in CI/CD pipelines.
# ============================================================

# 15. datetime.min and datetime.max
# Practical use case: Initialize variables for min/max log timestamps
oldest = datetime.max
newest = datetime.min
for ts in [datetime(2025, 9, 8), datetime(2025, 9, 9), datetime(2025, 9, 7)]:
    if ts < oldest:
        oldest = ts
    if ts > newest:
        newest = ts
print("Oldest log:", oldest, "Newest log:", newest)
# 👉 Why useful:
# Helps determine time range of log files, useful in monitoring and reporting.
# ============================================================
