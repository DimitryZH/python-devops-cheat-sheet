# ============================================================
# Practical use cases: Ansible automation with Python
# ============================================================

import subprocess
import os
import json

# 1. Run a simple Ansible ad-hoc command
# Practical use case: Ping all hosts in inventory
subprocess.run(["ansible", "all", "-i", "inventory.ini", "-m", "ping"])
# 👉 Why useful:
# Quick connectivity check before running big playbooks.
# ============================================================

# 2. Run a playbook
# Practical use case: Automate server configuration
subprocess.run(["ansible-playbook", "-i", "inventory.ini", "site.yml"])
# 👉 Why useful:
# Standard way to provision servers and apps in DevOps pipelines.
# ============================================================

# 3. Limit execution to a single host
# Practical use case: Run playbook only on one machine
subprocess.run(["ansible-playbook", "-i", "inventory.ini", "site.yml", "--limit", "web1"])
# 👉 Why useful:
# Target specific hosts without changing the inventory.
# ============================================================

# 4. Pass extra variables
# Practical use case: Override defaults dynamically
subprocess.run([
    "ansible-playbook", "-i", "inventory.ini", "deploy.yml",
    "--extra-vars", "env=prod version=1.2.3"
])
# 👉 Why useful:
# Easily inject environment or release version into playbooks.
# ============================================================

# 5. Use environment variables for secrets
# Practical use case: Secure password injection
os.environ["ANSIBLE_VAULT_PASSWORD_FILE"] = "./.vault_pass.txt"
print("Vault password configured via environment variable")
# 👉 Why useful:
# Secure handling of secrets in automation scripts.
# ============================================================

# 6. Run a playbook in check mode
# Practical use case: Dry-run to preview changes
subprocess.run(["ansible-playbook", "-i", "inventory.ini", "deploy.yml", "--check"])
# 👉 Why useful:
# Validate changes without modifying real infrastructure.
# ============================================================

# 7. Run with increased verbosity
# Practical use case: Debug failing playbooks
subprocess.run(["ansible-playbook", "-i", "inventory.ini", "site.yml", "-vvv"])
# 👉 Why useful:
# Get detailed logs for troubleshooting automation.
# ============================================================

# 8. Generate JSON output
# Practical use case: Parse results in Python
result = subprocess.run(
    ["ansible", "all", "-i", "inventory.ini", "-m", "setup", "--tree", "facts"],
    capture_output=True, text=True
)
print("Raw output:", result.stdout[:200], "...")
# 👉 Why useful:
# Machine-readable results for further automation.
# ============================================================

# 9. Run a playbook with tags
# Practical use case: Execute only specific tasks
subprocess.run(["ansible-playbook", "-i", "inventory.ini", "site.yml", "--tags", "deploy"])
# 👉 Why useful:
# Run just part of the automation without executing everything.
# ============================================================

# 10. Skip tasks with tags
# Practical use case: Exclude heavy tasks during dev
subprocess.run(["ansible-playbook", "-i", "inventory.ini", "site.yml", "--skip-tags", "db"])
# 👉 Why useful:
# Faster runs in test environments by skipping unnecessary tasks.
# ============================================================

# 11. Use dynamic inventory
# Practical use case: Get hosts from cloud provider
subprocess.run(["ansible", "all", "-i", "aws_ec2.yml", "-m", "ping"])
# 👉 Why useful:
# No need to maintain static inventory files in dynamic clouds.
# ============================================================

# 12. Encrypt sensitive files with Vault
# Practical use case: Protect secrets
subprocess.run(["ansible-vault", "encrypt", "secrets.yml"])
# 👉 Why useful:
# Ensures API keys and passwords are safe in git repos.
# ============================================================

# 13. Decrypt secrets before use
# Practical use case: Access protected vars
subprocess.run(["ansible-vault", "decrypt", "secrets.yml"])
# 👉 Why useful:
# Decrypted temporarily only when needed in automation.
# ============================================================

# 14. Test playbooks with ansible-lint
# Practical use case: Ensure best practices
subprocess.run(["ansible-lint", "site.yml"])
# 👉 Why useful:
# Prevents mistakes before deploying to production.
# ============================================================

# 15. Integrate with CI/CD pipeline
# Practical use case: Run playbooks in Jenkins/GitHub Actions
print("Ansible automation complete - ready for CI/CD integration")
# 👉 Why useful:
# Infrastructure as Code workflows become fully automated.
# ============================================================
