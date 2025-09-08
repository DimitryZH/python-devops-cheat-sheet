# ============================================================
# Practical use cases: Working with lists in DevOps
# ============================================================

# 1. list comprehension
# Practical use case: Filtering logs to get only errors
logs = [
    "INFO: Deployment started",
    "ERROR: Failed to pull Docker image",
    "INFO: Retrying connection",
    "ERROR: Timeout while connecting to database"
]
error_logs = [log for log in logs if "ERROR" in log]
print("Filtered error logs:", error_logs)
# 👉 Why useful:
# When analyzing logs from Kubernetes, Docker, or CI/CD pipelines,
# you often want to filter only ERROR messages for reporting or alerting.
# ==========================================================================

# 2. sorted()
# Practical use case: Sorting timestamps in logs
timestamps = ["2025-09-08 10:02:15", "2025-09-08 09:59:00", "2025-09-08 10:10:45"]
sorted_timestamps = sorted(timestamps)
print("Sorted timestamps:", sorted_timestamps)
# 👉 Why useful:
# Sorting logs by time helps you trace the order of events,
# especially when troubleshooting incidents across distributed systems.
# ==========================================================================

# 3. dict.fromkeys()
# Practical use case: Removing duplicates from a list while keeping order
ips = ["10.0.0.1", "10.0.0.2", "10.0.0.1", "10.0.0.3", "10.0.0.2"]
unique_ips = list(dict.fromkeys(ips))
print("Unique IPs:", unique_ips)
# 👉 Why useful:
# When collecting IPs from logs or monitoring tools,
# duplicates often appear. Removing them helps build a clean inventory
# (e.g., for firewall rules or monitoring dashboards).
# ==========================================================================

# 4. list comprehension + split()
# Practical use case: Extract container names from image tags
containers = ["nginx:latest", "redis:6", "mysql:8.0"]
container_names = [c.split(":")[0] for c in containers]
print("Container names:", container_names)
# 👉 Why useful:
# Helps normalize data — extracting only service names from image tags
# when comparing against deployment manifests.
# ==========================================================================

# 5. membership operator (in)
# Practical use case: Checking if a list contains a specific element
services = ["nginx", "redis", "postgres"]
if "nginx" in services:
    print("nginx is deployed")
# 👉 Why useful:
# Simple membership checks allow you to confirm if a specific service
# is running or included in a configuration before applying updates.
# ==========================================================================

# 6. slicing
# Practical use case: Splitting a list into batches
servers = ["web1", "web2", "web3", "web4", "web5", "web6"]
batch_size = 2
batches = [servers[i:i + batch_size] for i in range(0, len(servers), batch_size)]
print("Server batches:", batches)
# 👉 Why useful:
# Useful for rolling updates or batch deployments,
# processing a few servers at a time to reduce downtime and risk.
# ==========================================================================

# 7. nested list comprehension
# Practical use case: Flattening a list of lists
deployment_results = [
    ["success", "success"],
    ["failure"],
    ["success", "failure"]
]
flattened = [item for sublist in deployment_results for item in sublist]
print("Flattened results:", flattened)
# 👉 Why useful:
# Combines nested lists from multiple servers or tasks into a single list
# for easier analysis, counting, or reporting.
# ==========================================================================

# 8. list comprehension + f-strings
# Practical use case: Mapping values in a list
ports = [80, 443, 8080]
ports_str = [f"Port-{p}" for p in ports]
print("Ports with prefix:", ports_str)
# 👉 Why useful:
# Helps format configuration or commands dynamically,
# e.g., generating firewall rules or Docker port mappings.
# ==========================================================================

# 9. zip() + dict()
# Practical use case: Zipping two lists together
hosts = ["web1", "web2", "web3"]
ips = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]
host_ip_mapping = dict(zip(hosts, ips))
print("Host to IP mapping:", host_ip_mapping)
# 👉 Why useful:
# Quickly create mappings between resources (servers, containers, IPs)
# Useful in inventory management or generating configuration files.
# ==========================================================================

# 10. enumerate()
# Practical use case: Enumerate for indexing items
services = ["nginx", "redis", "postgres"]
for idx, service in enumerate(services, start=1):
    print(f"{idx}. {service}")
# 👉 Why useful:
# Enumerate helps you add numbering to tasks or logs,
# e.g., generating reports or ordered deployment instructions.
# ==========================================================================

# 11. slicing [::-1]
# Practical use case: Reversing a list
tasks = ["backup", "deploy", "monitor", "cleanup"]
reversed_tasks = tasks[::-1]
print("Reversed tasks:", reversed_tasks)
# 👉 Why useful:
# Useful for executing tasks in reverse order,
# e.g., rolling back deployments or undoing configuration changes.
# ==========================================================================

# 12. max() / min()
# Practical use case: Finding max/min values in a list
response_times = [120, 250, 95, 300, 180]  # in milliseconds
max_time = max(response_times)
min_time = min(response_times)
print(f"Max response time: {max_time} ms, Min response time: {min_time} ms")
# 👉 Why useful:
# Quickly identify performance bottlenecks or outliers in metrics,
# like API response times, load times, or task durations.
# ==========================================================================

# 13. sum()
# Practical use case: Summing numeric values
cpu_usage = [10, 20, 30, 40, 50]  # in percent
total_cpu = sum(cpu_usage)
print("Total CPU usage:", total_cpu)
# 👉 Why useful:
# Summing metrics helps you monitor resource usage across servers
# and can be used for alerting or scaling decisions.
# ==========================================================================

# 14. concatenation (+)
# Practical use case: Combining lists
frontend_services = ["nginx", "haproxy"]
backend_services = ["redis", "postgres"]
all_services = frontend_services + backend_services
print("All services:", all_services)
# 👉 Why useful:
# Easily merge multiple resource lists for deployment or inventory tasks,
# e.g., generating a single list of all services in your environment.
# ==========================================================================

# 15. any() / all()
# Practical use case: Conditional checks across a list
checks = [True, True, False]
print("Any failures?", any(checks))
print("All passed?", all(checks))
# 👉 Why useful:
# Useful for quickly evaluating health checks or task results
# across multiple servers or containers.
# any() returns True if at least one is True, all() returns True only if all are True.
