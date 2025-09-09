# ============================================================
# Practical use cases: Working with tuples in DevOps
# ============================================================

# 1. Tuple creation
# Practical use case: Store server info as immutable data
server_info = ("web1", "192.168.1.10", "running")
print("Server info:", server_info)
# 👉 Why useful:
# Tuples are immutable, making them safe for representing static records.
# ==============================================================================

# 2. Indexing
# Practical use case: Access specific data from server info
ip_address = server_info[1]
print("Server IP:", ip_address)
# 👉 Why useful:
# Quick structured access to ordered data like configs or logs.
# ==============================================================================

# 3. Tuple unpacking
# Practical use case: Extract server details
(name, ip, status) = server_info
print(f"Name={name}, IP={ip}, Status={status}")
# 👉 Why useful:
# Simplifies code readability when working with structured configs.
# ==============================================================================

# 4. Nested tuples
# Practical use case: Group servers with their ports
server_ports = (("web1", 80), ("web2", 443))
print("Server and ports:", server_ports)
# 👉 Why useful:
# Compact way to represent resource mappings (server → port, host → service).
# ==============================================================================

# 5. len()
# Practical use case: Count number of servers
print("Number of server-port pairs:", len(server_ports))
# 👉 Why useful:
# Useful for quick validations in inventory or monitoring.
# ==============================================================================

# 6. in operator
# Practical use case: Check if a server exists in records
if ("web1", 80) in server_ports:
    print("web1:80 is present")
# 👉 Why useful:
# Fast membership testing in structured configs.
# ==============================================================================

# 7. Tuples as dictionary keys
# Practical use case: Map (server, port) to status
status_map = {("web1", 80): "ok", ("web2", 443): "down"}
print("Status of web2:443:", status_map[("web2", 443)])
# 👉 Why useful:
# Tuples are hashable, great for composite keys in dictionaries.
# ==============================================================================

# 8. Immutability benefit
# Practical use case: Protect configs from accidental modification
immutable_config = ("db1", "10.0.0.5", "primary")
# immutable_config[1] = "10.0.0.6"  # ❌ Error if uncommented
print("Immutable config:", immutable_config)
# 👉 Why useful:
# Ensures critical deployment parameters can’t be altered during runtime.
# ==============================================================================

# 9. Multiple assignment
# Practical use case: Return multiple values from function
def get_server_stats():
    return ("web1", "running", 0.3)

name, status, load = get_server_stats()
print(f"Server {name} is {status}, load={load}")
# 👉 Why useful:
# Tuples make it easy to return and unpack multiple results in automation tasks.
# ==============================================================================

# 10. zip() with tuples
# Practical use case: Combine servers and IPs
servers = ("web1", "web2", "web3")
ips = ("192.168.1.10", "192.168.1.11", "192.168.1.12")
combined = tuple(zip(servers, ips))
print("Server-IP pairs:", combined)
# 👉 Why useful:
# Quickly build mappings (e.g., hostnames → IPs) for deployment scripts.
# ==============================================================================

# 11. sorted()
# Practical use case: Sort tuples by server name
sorted_servers = sorted(combined, key=lambda x: x[0])
print("Sorted servers:", sorted_servers)
# 👉 Why useful:
# Helps organize data for reporting or consistent config generation.
# ==============================================================================