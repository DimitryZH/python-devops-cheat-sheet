# ============================================================
# Practical use cases: Using os and sys modules in DevOps
# ============================================================

import os
import sys


# 1. os.getenv()
# Practical use case: Work with environment variables
db_host = os.getenv("DB_HOST", "localhost")
print("Database host:", db_host)
# 👉 Why useful:
# Reading env variables is key for CI/CD pipelines and secrets management.
# ============================================================

# 2. os.environ
# Practical use case: Set environment variable inside script
os.environ["API_KEY"] = "supersecret"
print("API_KEY from env:", os.environ.get("API_KEY"))
# 👉 Why useful:
# Useful for injecting variables into subprocesses, tests, or containerized apps.
# ============================================================

# 3. os.getcwd()
# Practical use case: Get current working directory
cwd = os.getcwd()
print("Current working directory:", cwd)
# 👉 Why useful:
# Helps scripts adapt dynamically without hardcoding file paths.
# ============================================================

# 4. os.listdir()
# Practical use case: List files in a directory
files = os.listdir(".")
print("Files in current directory:", files)
# 👉 Why useful:
# Useful for checking generated logs, configs, or build artifacts.
# ============================================================

# 5. os.path.exists()
# Practical use case: Check if config file exists
if os.path.exists("config.yaml"):
    print("Config file exists")
else:
    print("Config file missing")
# 👉 Why useful:
# Ensures scripts don’t fail if a required file is missing.
# ============================================================

# 6. os.makedirs()
# Practical use case: Create nested directories for backups
backup_dir = "backups/2025-09-09"
os.makedirs(backup_dir, exist_ok=True)
print("Backup directory created:", backup_dir)
# 👉 Why useful:
# Automatically prepares directories for logs, reports, or backups.
# ============================================================

# 7. os.remove()
# Practical use case: Clean up old log file
log_file = "old.log"
if os.path.exists(log_file):
    os.remove(log_file)
    print("Removed old log file")
# 👉 Why useful:
# Automates cleanup of temporary files before new deployments.
# ============================================================

# 8. os.rename()
# Practical use case: Rotate log file
if os.path.exists("app.log"):
    os.rename("app.log", "app.log.bak")
    print("Rotated log file")
# 👉 Why useful:
# Simple log rotation without external tools.
# ============================================================

# 9. sys.exit()
# Practical use case: Exit with status code
if db_host == "localhost":
    print("Warning: using default DB host")
    sys.exit(1)
# 👉 Why useful:
# Exit codes are critical for CI/CD tools like Jenkins, Ansible, or GitHub Actions.
# ============================================================

# 10. sys.argv
# Practical use case: Read arguments passed to script
print("Script arguments:", sys.argv)
# 👉 Why useful:
# Lets scripts behave dynamically depending on provided parameters.
# ============================================================

# 11. sys.path
# Practical use case: Add custom path for module imports
sys.path.append("/opt/custom_modules")
print("Updated sys.path:", sys.path[-1])
# 👉 Why useful:
# Useful in automation when modules are not in standard locations.
# ============================================================

# 12. os.system()
# Practical use case: Quick command execution
os.system("echo 'Hello from os.system'")
# 👉 Why useful:
# Lightweight way to run commands, though subprocess is safer.
# ============================================================

# 13. os.cpu_count()
# Practical use case: Detect available CPU cores
print("Available CPUs:", os.cpu_count())
# 👉 Why useful:
# Useful for tuning parallel builds, thread pools, or resource allocation.
# ============================================================

# 14. os.uname() (Linux/Unix only)
# Practical use case: Print system information
if hasattr(os, "uname"):
    print("System info:", os.uname())
# 👉 Why useful:
# Helps identify environment details during troubleshooting or audits.
# ============================================================

# 15. sys.version
# Practical use case: Print Python version
print("Python version:", sys.version)
# 👉 Why useful:
# Verifies runtime version in environments with multiple Python installations.
# ============================================================
