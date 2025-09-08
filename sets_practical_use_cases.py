# ============================================================
# Practical use cases: Working with sets in DevOps
# ============================================================

# 1. set creation
# Practical use case: Creating a set of servers
servers = {"web1", "web2", "web3", "web1"}
print("Unique servers:", servers)
# 👉 Why useful:
# Sets automatically remove duplicates, useful for building inventories
# from logs or monitoring outputs.
# ==============================================================================

# 2. add()
# Practical use case: Add a new server dynamically
servers.add("web4")
print("Updated servers:", servers)
# 👉 Why useful:
# Dynamically track new resources discovered during automation scripts.
# ==============================================================================

# 3. remove()
# Practical use case: Remove a server from inventory
servers.remove("web2")
print("Servers after removal:", servers)
# 👉 Why useful:
# Remove decommissioned or failed servers from tracking.
# ==============================================================================

# 4. discard()
# Practical use case: Remove a server safely without KeyError
servers.discard("web5")
print("Servers after discard:", servers)
# 👉 Why useful:
# Safe removal when unsure if item exists, preventing script errors.
# ==============================================================================

# 5. union()
# Practical use case: Combine servers from multiple environments
env1 = {"web1", "web2"}
env2 = {"web2", "web3"}
all_servers = env1.union(env2)
print("All servers:", all_servers)
# 👉 Why useful:
# Merge inventories without duplicates, e.g., staging + production.
# ==============================================================================

# 6. intersection()
# Practical use case: Find common servers between two deployments
common_servers = env1.intersection(env2)
print("Common servers:", common_servers)
# 👉 Why useful:
# Identify servers that exist in both environments, useful for consistency checks.
# ==============================================================================

# 7. difference()
# Practical use case: Find servers present in env1 but not in env2
unique_env1 = env1.difference(env2)
print("Servers only in env1:", unique_env1)
# 👉 Why useful:
# Track servers that need updates or maintenance.
# ==============================================================================

# 8. symmetric_difference()
# Practical use case: Find servers that differ between two environments
diff_servers = env1.symmetric_difference(env2)
print("Servers differing between env1 and env2:", diff_servers)
# 👉 Why useful:
# Quickly see discrepancies for auditing or configuration drift detection.
# ==============================================================================

# 9. in operator
# Practical use case: Check if a server exists in a set
if "web1" in servers:
    print("web1 is active")
# 👉 Why useful:
# Fast membership test, useful for validation before performing tasks.
# ==============================================================================

# 10. len()
# Practical use case: Count the number of unique servers
print("Total unique servers:", len(servers))
# 👉 Why useful:
# Monitoring or reporting the size of environments, useful for scaling decisions.
# ==============================================================================

# 11. set comprehension
# Practical use case: Generate a set of ports from service definitions
service_ports = [80, 443, 80, 22]
unique_ports = {p for p in service_ports}
print("Unique ports:", unique_ports)
# 👉 Why useful:
# Quickly filter unique values for firewall rules, deployments, or inventory.
# ==============================================================================

# 12. clear()
# Practical use case: Reset the set of servers before a new scan
servers.clear()
print("Servers after clear:", servers)
# 👉 Why useful:
# Useful when refreshing inventories or cleaning temporary data.
