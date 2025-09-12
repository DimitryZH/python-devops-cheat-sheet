# ============================================================
# # Practical use cases: Working with files in DevOps
# ============================================================

# 1. open() with read()
# Practical use case: Read log file contents
with open("app.log", "r") as f:
    logs = f.read()
print("Log contents:\n", logs)
# 👉 Why useful:
# Quickly read logs, configs, or state files during automation.
# ============================================================

# 2. open() with write()
# Practical use case: Save deployment output
with open("deploy.log", "w") as f:
    f.write("Deployment finished successfully\n")
print("Deployment log created")
# 👉 Why useful:
# Store deployment results or process logs for later analysis.
# ============================================================

# 3. open() with append
# Practical use case: Add new log entry
with open("deploy.log", "a") as f:
    f.write("New service deployed at port 8080\n")
print("Appended new log entry")
# 👉 Why useful:
# Preserve existing logs while adding new records.
# ============================================================

# 4. readlines()
# Practical use case: Process log lines one by one
with open("app.log", "r") as f:
    lines = f.readlines()
for line in lines:
    if "ERROR" in line:
        print("Found error:", line.strip())
# 👉 Why useful:
# Helps filter specific events (errors, warnings) from logs.
# ============================================================

# 5. with statement
# Practical use case: Auto-close file after use
with open("config.yaml", "r") as f:
    config_data = f.read()
print("Config data read safely")
# 👉 Why useful:
# Avoids forgetting f.close(), prevents resource leaks in scripts.
# ============================================================

# 6. os.path.exists()
# Practical use case: Check if file exists before reading
import os
if os.path.exists("secrets.env"):
    print("Secrets file exists")
# 👉 Why useful:
# Prevents crashes in automation if required files are missing.
# ============================================================

# 7. os.remove()
# Practical use case: Remove temporary file
temp_file = "temp.txt"
with open(temp_file, "w") as f:
    f.write("temporary data")
os.remove(temp_file)
print("Temporary file removed")
# 👉 Why useful:
# Clean up after builds, deployments, or temporary tasks.
# ============================================================

# 8. pathlib for paths
# Practical use case: Handle cross-platform file paths
from pathlib import Path
log_path = Path("logs/app.log")
print("Log file name:", log_path.name)
print("Parent folder:", log_path.parent)
# 👉 Why useful:
# Safer and cleaner path handling than manual string operations.
# ============================================================

# 9. Write list of lines
# Practical use case: Save inventory file
servers = ["web1\n", "web2\n", "web3\n"]
with open("inventory.txt", "w") as f:
    f.writelines(servers)
print("Inventory saved")
# 👉 Why useful:
# Quickly generate inventory or host files for Ansible, Terraform, etc.
# ============================================================

# 10. Read large file line by line
# Practical use case: Process huge logs without memory issues
with open("big.log", "r") as f:
    for line in f:
        if "CRITICAL" in line:
            print("Critical issue:", line.strip())
# 👉 Why useful:
# Efficiently handle logs or data streams without loading into memory.
# ============================================================

# 11. json.dump() / json.load()
# Practical use case: Save and load structured configs
import json
data = {"service": "api", "status": "running"}
with open("config.json", "w") as f:
    json.dump(data, f)
with open("config.json", "r") as f:
    loaded = json.load(f)
print("Loaded config:", loaded)
# 👉 Why useful:
# JSON is the standard for APIs, configs, and IaC tools.
# ============================================================

# 12. tempfile
# Practical use case: Create temp files safely
import tempfile
with tempfile.NamedTemporaryFile(delete=True) as tf:
    tf.write(b"temporary secret")
    print("Temp file created:", tf.name)
# 👉 Why useful:
# Avoids name collisions and ensures cleanup of sensitive files.
# ============================================================

# 13. shutil.copy()
# Practical use case: Backup config file
import shutil
shutil.copy("config.json", "config_backup.json")
print("Config backed up")
# 👉 Why useful:
# Useful for backup/restore of configs before deployments.
# ============================================================

# 14. File modes
# Practical use case: Demonstrate read/write modes
with open("example.txt", "w+") as f:
    f.write("Hello DevOps\n")
    f.seek(0)
    print("File content:", f.read())
# 👉 Why useful:
# Understanding modes is critical for proper file operations.
# ============================================================

# 15. Handling file not found
# Practical use case: Safe file access
try:
    with open("nonexistent.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found, skipping")
# 👉 Why useful:
# Prevents scripts from crashing when expected files don’t exist.
# Useful for log processing, config management, and file-based state handling.


