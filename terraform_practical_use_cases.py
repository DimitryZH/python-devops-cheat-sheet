# ============================================================
# Practical use cases: Terraform automation with Python
# ============================================================

import subprocess
import os
import json

# 1. Set working directory
# Practical use case: Define path to Terraform project
tf_dir = "./terraform_project"
# 👉 Why useful:
# Central place for running all Terraform commands.
# ============================================================

# 2. Initialize Terraform
# Practical use case: Prepare backend and modules
try:
    subprocess.run(["terraform", "init"], cwd=tf_dir, check=True)
    print("Terraform initialized successfully")
except subprocess.CalledProcessError as e:
    print("Terraform init failed:", e)
# 👉 Why useful:
# Required first step before applying Terraform configs.
# ============================================================

# 3. Validate Terraform configuration
# Practical use case: Catch syntax errors early
try:
    subprocess.run(["terraform", "validate"], cwd=tf_dir, check=True)
    print("Terraform configuration is valid")
except subprocess.CalledProcessError as e:
    print("Validation failed:", e)
# 👉 Why useful:
# Detects broken configurations before deployment.
# ============================================================

# 4. Format Terraform code
# Practical use case: Enforce consistent style
subprocess.run(["terraform", "fmt"], cwd=tf_dir)
print("Terraform code formatted")
# 👉 Why useful:
# Ensures readable, maintainable configs in teams.
# ============================================================

# 5. Plan infrastructure changes
# Practical use case: Preview changes before applying
try:
    result = subprocess.run(
        ["terraform", "plan", "-out=tfplan"], cwd=tf_dir, capture_output=True, text=True, check=True
    )
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print("Terraform plan failed:", e)
# 👉 Why useful:
# Safe preview of what Terraform will create, change, or destroy.
# ============================================================

# 6. Apply changes
# Practical use case: Deploy infrastructure
try:
    subprocess.run(["terraform", "apply", "-auto-approve"], cwd=tf_dir, check=True)
    print("Infrastructure applied successfully")
except subprocess.CalledProcessError as e:
    print("Terraform apply failed:", e)
# 👉 Why useful:
# Automates actual infrastructure provisioning.
# ============================================================

# 7. Destroy infrastructure
# Practical use case: Clean up resources
try:
    subprocess.run(["terraform", "destroy", "-auto-approve"], cwd=tf_dir, check=True)
    print("Infrastructure destroyed")
except subprocess.CalledProcessError as e:
    print("Terraform destroy failed:", e)
# 👉 Why useful:
# Tear down test environments automatically.
# ============================================================

# 8. Show current state
# Practical use case: Inspect deployed resources
result = subprocess.run(["terraform", "show", "-json"], cwd=tf_dir, capture_output=True, text=True)
try:
    state = json.loads(result.stdout)
    print("Terraform state resources:", [res["address"] for res in state.get("values", {}).get("root_module", {}).get("resources", [])])
except json.JSONDecodeError:
    print("Failed to parse state output")
# 👉 Why useful:
# Programmatically consume deployed resource details.
# ============================================================

# 9. Output variables
# Practical use case: Get outputs from Terraform
result = subprocess.run(["terraform", "output", "-json"], cwd=tf_dir, capture_output=True, text=True)
try:
    outputs = json.loads(result.stdout)
    print("Terraform outputs:", outputs)
except json.JSONDecodeError:
    print("Failed to parse outputs")
# 👉 Why useful:
# Pass values (IP, DNS, secrets) to CI/CD pipelines.
# ============================================================

# 10. Use environment variables
# Practical use case: Inject sensitive values
os.environ["TF_VAR_db_password"] = "supersecret"
print("Environment variable set for Terraform")
# 👉 Why useful:
# Secure handling of secrets without hardcoding.
# ============================================================

# 11. Work with workspaces
# Practical use case: Separate environments (dev, prod)
subprocess.run(["terraform", "workspace", "new", "dev"], cwd=tf_dir)
subprocess.run(["terraform", "workspace", "select", "dev"], cwd=tf_dir)
print("Workspace switched to dev")
# 👉 Why useful:
# Isolates environments in the same configuration.
# ============================================================

# 12. Run with detailed logging
# Practical use case: Debug automation
os.environ["TF_LOG"] = "DEBUG"
print("Terraform debug logging enabled")
# 👉 Why useful:
# Helps troubleshoot failed automation pipelines.
# ============================================================

# 13. Handle errors gracefully
# Practical use case: Prevent pipeline crashes
try:
    subprocess.run(["terraform", "plan"], cwd=tf_dir, check=True)
except subprocess.CalledProcessError:
    print("Plan failed but script continues")
# 👉 Why useful:
# Makes automation more resilient in CI/CD.
# ============================================================

# 14. Automate drift detection
# Practical use case: Detect manual changes
result = subprocess.run(["terraform", "plan"], cwd=tf_dir, capture_output=True, text=True)
if "No changes." not in result.stdout:
    print("Drift detected in infrastructure")
# 👉 Why useful:
# Ensures infrastructure matches code definition.
# ============================================================

# 15. Integrate with CI/CD
# Practical use case: Run Terraform in pipelines
print("Terraform automation complete - ready for Jenkins/GitHub Actions")
# 👉 Why useful:
# Infrastructure as Code is best executed in CI/CD.
# ============================================================
