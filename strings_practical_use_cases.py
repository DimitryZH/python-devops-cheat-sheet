# ============================================================
# Python String Methods. Practical use cases for DevOps and SRE
# ============================================================

# 1. strip()
# Practical use case: Remove unnecessary spaces when parsing config lines or API responses

config_line = "   value=42   "
cleaned = config_line.strip()
print(cleaned)  # "value=42"

# 👉 Why useful:
# Avoids errors when reading config files or API responses with extra whitespace.
# Critical for parsing usernames, file paths, or values from environment variables.
# =============================================================================================

# 2. replace()
# Practical use case: Replace placeholders in configuration or YAML manifests

nginx_conf = "server_name PLACEHOLDER;"
updated = nginx_conf.replace("PLACEHOLDER", "myapp.local")
print(updated)  # "server_name myapp.local;"

# 👉 Why useful:
# Quick way to modify configs or manifests before deploying them
# (e.g., replacing placeholders in nginx.conf or Kubernetes YAML).
# Works well for small automation scripts without using a templating engine.
# =============================================================================================

# 3. split()
# Practical use case: Parse log entries into fields (level, message, path)

log_entry = "ERROR:disk full:/dev/sda1"
parts = log_entry.split(":")
print(parts)  # ["ERROR", "disk full", "/dev/sda1"]

# 👉 Why useful:
# Allows easy extraction of log levels, messages, or timestamps.
# Essential for monitoring scripts, alerts, or automated log processing.
# =============================================================================================

# 4. join()
# Practical use case: Build command strings from list of commands or paths

commands = ["systemctl", "restart", "nginx"]
cmd = " ".join(commands)
print(cmd)  # "systemctl restart nginx"

# 👉 Why useful:
# Efficient way to combine list items into strings.
# Common in building dynamic shell commands, paths, or environment variables.
# =============================================================================================

# 5. startswith()
# Practical use case: Detect log lines starting with ERROR or WARNING

line = "ERROR: something went wrong"
print(line.startswith("ERROR"))  # True

# 👉 Why useful:
# Helps filter specific log lines or validate commands.
# Useful in scripts that trigger alerts on errors.
# =============================================================================================

# 6. endswith()
# Practical use case: Detect file types by extension (e.g., .log, .gz)

filename = "backup.tar.gz"
print(filename.endswith(".gz"))  # True

# 👉 Why useful:
# Quickly identify file types in automation scripts.
# Useful for backup management, log rotation, or selective file processing.
# =============================================================================================

# 7. find()
# Practical use case: Locate substring position in logs or configuration

log = "User admin logged in"
pos = log.find("admin")
print(pos)  # 5

# 👉 Why useful:
# Locate keywords or identifiers in text without raising exceptions.
# Useful for searching logs, configs, or API responses.
# =============================================================================================

# 8. in (membership operator)
# Practical use case: Quick check if keyword exists in log line or command output

line = "connection from 10.0.0.5 established"
print("10.0.0.5" in line)  # True

# 👉 Why useful:
# Simple and readable way to detect presence of substrings.
# Common in monitoring scripts, firewall checks, or parsing outputs.
# =============================================================================================

# 9. count()
# Practical use case: Count how many times a specific event occurs in logs

log = "failed login from 10.0.0.1 failed login from 10.0.0.2"
failed_count = log.count("failed")
print(failed_count)  # 2

# 👉 Why useful:
# Helps quickly analyze logs or text streams.
# Count occurrences of errors, failed logins, or warnings in monitoring scripts.
# =============================================================================================

# 10. upper()
# Practical use case: Normalize environment variable names or config keys

env = "path"
normalized = env.upper()
print(normalized)  # "PATH"

# 👉 Why useful:
# Ensures consistency in environment variables or configuration keys.
# Avoids errors due to case sensitivity in scripts or automation pipelines.
# =============================================================================================

# 11. lower()
# Practical use case: Normalize usernames, emails, or hostnames to avoid mismatches

raw_user = "Admin"
username = raw_user.lower()
print(username)  # "admin"

# 👉 Why useful:
# Standardizes inputs to avoid mismatches.
# Essential for authentication, email handling, or hostname normalization.
# =============================================================================================

# 12. f-strings
# Practical use case: Dynamically generate commands, paths, or config snippets

service = "nginx"
cmd = f"systemctl restart {service}"
print(cmd)  # "systemctl restart nginx"

# 👉 Why useful:
# Fastest and cleanest way to embed variables into strings.
# Crucial for generating dynamic commands, paths, or configuration snippets.
# =============================================================================================

# 13. format()
# Practical use case: Generate configuration text from template with variables
template = "server_name={name}\nport={port}"
config = template.format(name="app02", port=8081)
print(config)
# server_name=app02
# port=8081

# 👉 Why useful:
# Flexible for template-based configuration generation.
# Ideal for automation scripts that produce multiple configuration files (nginx, systemd, Kubernetes YAML).
