# ============================================================
# Practical use cases: Using Python modules in DevOps
# ============================================================

# 1. import os
# Practical use case: Work with environment variables
import os
db_host = os.getenv("DB_HOST", "localhost")
print("Database host:", db_host)
# 👉 Why useful:
# Reading env variables is key for CI/CD pipelines and secrets management.
# ============================================================

# 2. import sys
# Practical use case: Exit with status code
import sys
if db_host == "localhost":
    print("Warning: using default DB host")
    sys.exit(1)
# 👉 Why useful:
# Control script exit codes for automation tools like Jenkins, Ansible, or GitHub Actions.
# ============================================================

# 3. import subprocess
# Practical use case: Run shell commands
import subprocess
result = subprocess.run(["echo", "Hello DevOps"], capture_output=True, text=True)
print("Subprocess output:", result.stdout.strip())
# 👉 Why useful:
# Safely run CLI tools (kubectl, terraform, aws, az) from Python scripts.
# ============================================================

# 4. import json
# Practical use case: Parse JSON config
import json
json_data = '{"service": "api", "status": "running"}'
parsed = json.loads(json_data)
print("Parsed JSON:", parsed)
# 👉 Why useful:
# JSON is everywhere in APIs, Terraform state, Docker inspect, etc.
# ============================================================

# 5. import yaml (PyYAML, external package)
# Practical use case: Parse YAML config
try:
    import yaml
    yaml_data = """
    service: api
    replicas: 3
    """
    parsed_yaml = yaml.safe_load(yaml_data)
    print("Parsed YAML:", parsed_yaml)
except ImportError:
    print("PyYAML not installed, skipping example")
# 👉 Why useful:
# YAML is standard for Kubernetes manifests, Ansible playbooks, CI/CD configs.
# ============================================================

# 6. import pathlib
# Practical use case: Cross-platform file paths
from pathlib import Path
p = Path("logs/app.log")
print("File name:", p.name)
print("Parent folder:", p.parent)
# 👉 Why useful:
# Cleaner and safer path handling than manual string concatenation.
# ============================================================

# 7. import shutil
# Practical use case: Copy files
import shutil
shutil.copy("modules_practical_use_cases.py", "modules_copy.py")
print("File copied")
# 👉 Why useful:
# Backup configs, copy deployment artifacts, or manage temp files.
# ============================================================

# 8. import datetime
# Practical use case: Timestamp logs
from datetime import datetime
print("Current timestamp:", datetime.now().isoformat())
# 👉 Why useful:
# Timestamps are critical for logging, monitoring, and auditing.
# ============================================================

# 9. import time
# Practical use case: Retry with delay
import time
for i in range(3):
    print(f"Attempt {i+1}")
    time.sleep(2)
# 👉 Why useful:
# Implement retries/backoffs in automation scripts.
# ============================================================

# 10. import logging
# Practical use case: Structured logging
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Service started")
logging.error("Something went wrong")
# 👉 Why useful:
# Structured logging improves observability and integration with monitoring systems.
# ============================================================

# 11. import tempfile
# Practical use case: Temporary file for secrets
import tempfile
with tempfile.NamedTemporaryFile(delete=True) as tf:
    tf.write(b"secret-token")
    print("Created temp file:", tf.name)
# 👉 Why useful:
# Avoids leaving sensitive files behind after scripts finish.
# ============================================================

# 12. import argparse
# Practical use case: CLI arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--env", default="dev", help="Target environment")
args = parser.parse_args([])
print("Selected environment:", args.env)
# 👉 Why useful:
# Build CLI tools for deployments, migrations, and automation.
# ============================================================

# 13. import re
# Practical use case: Validate IP address
import re
ip = "192.168.1.10"
if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ip):
    print("Valid IP:", ip)
# 👉 Why useful:
# Regex is useful for validating configs, parsing logs, and enforcing naming conventions.
# ============================================================

# 14. import socket
# Practical use case: Check if port is open
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1)
try:
    s.connect(("127.0.0.1", 22))
    print("Port 22 open")
except Exception:
    print("Port 22 closed")
finally:
    s.close()
# 👉 Why useful:
# Check service availability during monitoring or health checks.
# ============================================================

# 15. import hashlib
# Practical use case: Verify file integrity
import hashlib
with open("modules_practical_use_cases.py", "rb") as f:
    file_hash = hashlib.sha256(f.read()).hexdigest()
print("SHA256 hash:", file_hash)
# 👉 Why useful:
# Ensures integrity of configs or artifacts in CI/CD pipelines.
