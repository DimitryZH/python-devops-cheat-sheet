# ============================================================
# Practical use cases: Working with dictionaries in DevOps
# ============================================================

# 1. Dictionary creation
# Practical use case: Store server configs
server_config = {
    "name": "web1",
    "ip": "192.168.1.10",
    "status": "running"
}
print("Server config:", server_config)
# 👉 Why useful:
# Dictionaries naturally represent JSON/YAML-style configs.
# =======================================================================

# 2. Access by key
# Practical use case: Get server IP
print("Server IP:", server_config["ip"])
# 👉 Why useful:
# Fast lookup of config parameters, similar to how env vars or manifests work.
# =======================================================================

# 3. get()
# Practical use case: Access optional values with default
print("Backup IP:", server_config.get("backup_ip", "not set"))
# 👉 Why useful:
# Prevents KeyError when keys may or may not exist in configs.
# =======================================================================

# 4. Update value
# Practical use case: Change server status
server_config["status"] = "maintenance"
print("Updated config:", server_config)
# 👉 Why useful:
# Reflects real-time state changes of resources.
# =======================================================================

# 5. Add new key
# Practical use case: Add monitoring metric
server_config["cpu_load"] = 0.85
print("Config with metric:", server_config)
# 👉 Why useful:
# Extend configs dynamically during automation scripts.
# =======================================================================

# 6. keys(), values(), items()
# Practical use case: Iterate over config
print("Keys:", list(server_config.keys()))
print("Values:", list(server_config.values()))
print("Items:", list(server_config.items()))
# 👉 Why useful:
# Essential for converting configs to text files, logs, or env variables.
# =======================================================================

# 7. Loop through dictionary
# Practical use case: Print server configs
for key, value in server_config.items():
    print(f"{key}: {value}")
# 👉 Why useful:
# Easy way to generate config files or debugging output.
# =======================================================================

# 8. Dictionary comprehension
# Practical use case: Convert IPs to uppercase (example transformation)
servers = {"web1": "192.168.1.10", "web2": "192.168.1.11"}
uppercased_ips = {name: ip.upper() for name, ip in servers.items()}
print("Uppercased IPs:", uppercased_ips)
# 👉 Why useful:
# Great for transforming configs, filtering data, or preparing manifests.
# =======================================================================

# 9. pop()
# Practical use case: Remove deprecated config key
status = server_config.pop("status", None)
print("Removed status:", status)
print("Config after removal:", server_config)
# 👉 Why useful:
# Clean up old config fields safely without crashing.
# =======================================================================

# 10. update()
# Practical use case: Merge new configs
new_config = {"status": "running", "region": "us-east-1"}
server_config.update(new_config)
print("Merged config:", server_config)
# 👉 Why useful:
# Easy way to apply updates or patches from external configs.
# =======================================================================

# 11. Nested dictionaries
# Practical use case: Store multiple servers
infra = {
    "web1": {"ip": "192.168.1.10", "status": "running"},
    "web2": {"ip": "192.168.1.11", "status": "down"},
}
print("Infrastructure:", infra)
print("web2 status:", infra["web2"]["status"])
# 👉 Why useful:
# Common structure for inventories (like Ansible hosts or Terraform state).
# =======================================================================

# 12. Dictionary as JSON
# Practical use case: Serialize to JSON
import json
print("Server config JSON:", json.dumps(server_config, indent=2))
# 👉 Why useful:
# Interact with APIs, save configs, or share state across tools.
# =======================================================================

# 13. dict.fromkeys()
# Practical use case: Initialize feature flags
features = dict.fromkeys(["logging", "monitoring", "alerts"], False)
print("Feature flags:", features)
# 👉 Why useful:
# Quick way to initialize config maps with default values.
# =======================================================================

# 14. setdefault()
# Practical use case: Ensure key exists
region = server_config.setdefault("region", "eu-west-1")
print("Region after setdefault:", region)
print("Config with region:", server_config)
# 👉 Why useful:
# Prevents overwriting if value already exists, good for defaults.
# =======================================================================

# 15. clear()
# Practical use case: Reset configs
temp_config = {"debug": True, "trace": True}
temp_config.clear()
print("Cleared config:", temp_config)
# 👉 Why useful:
# Safely empty a config dictionary during cleanup or teardown scripts.
