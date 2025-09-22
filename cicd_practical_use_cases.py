# ============================================================
# Practical use cases: CI/CD automation with Python
# ============================================================
# This file demonstrates how to automate CI/CD workflows using Python.
# Focus on GitHub Actions, Jenkins, GitLab CI, Docker, Kubernetes, and pipeline management.
# ============================================================

import os
import subprocess
import requests
import json
from datetime import datetime

# 1. Trigger a GitHub Actions workflow via API
# Practical use case: Start a workflow from a Python script
def trigger_github_actions(repo, workflow_id, token):
    url = f"https://api.github.com/repos/{repo}/actions/workflows/{workflow_id}/dispatches"
    headers = {"Authorization": f"token {token}"}
    data = {"ref": "main"}
    response = requests.post(url, headers=headers, json=data)
    return response.status_code
# 👉 Why useful:
# Automates deployment pipelines without manually visiting GitHub.

# ============================================================

# 2. Check GitHub Actions workflow status
# Practical use case: Monitor workflow execution
def check_github_workflow_status(repo, run_id, token):
    url = f"https://api.github.com/repos/{repo}/actions/runs/{run_id}"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    return response.json()
# 👉 Why useful:
# Provides status updates programmatically for CI/CD dashboards.

# ============================================================

# 3. Trigger Jenkins job
# Practical use case: Start Jenkins job via Python
def trigger_jenkins_job(url, job_name, user, token):
    job_url = f"{url}/job/{job_name}/build"
    response = requests.post(job_url, auth=(user, token))
    return response.status_code
# 👉 Why useful:
# Integrates Jenkins jobs into Python-based automation scripts.

# ============================================================

# 4. Get Jenkins job status
# Practical use case: Check last build result
def get_jenkins_job_status(url, job_name, user, token):
    job_url = f"{url}/job/{job_name}/lastBuild/api/json"
    response = requests.get(job_url, auth=(user, token))
    return response.json()
# 👉 Why useful:
# Enables monitoring and reporting of Jenkins pipelines automatically.

# ============================================================

# 5. Trigger GitLab CI pipeline
# Practical use case: Start pipeline via API
def trigger_gitlab_pipeline(project_id, token, ref="main"):
    url = f"https://gitlab.com/api/v4/projects/{project_id}/trigger/pipeline"
    data = {"token": token, "ref": ref}
    response = requests.post(url, data=data)
    return response.json()
# 👉 Why useful:
# Automates deployments in GitLab CI/CD without manual triggers.

# ============================================================

# 6. Monitor GitLab pipeline status
# Practical use case: Check pipeline execution
def get_gitlab_pipeline_status(project_id, pipeline_id, token):
    url = f"https://gitlab.com/api/v4/projects/{project_id}/pipelines/{pipeline_id}"
    headers = {"PRIVATE-TOKEN": token}
    response = requests.get(url, headers=headers)
    return response.json()
# 👉 Why useful:
# Provides programmatic access to pipeline states for alerts or dashboards.

# ============================================================

# 7. Run tests before deployment
# Practical use case: Execute unit tests automatically
def run_unit_tests():
    result = subprocess.run(
        ["pytest", "--maxfail=1", "--disable-warnings", "-q"],
        capture_output=True, text=True
    )
    return result.stdout
# 👉 Why useful:
# Ensures code quality before deployment in automated pipelines.

# ============================================================

# 8. Build Docker image as part of pipeline
# Practical use case: Package application in container
def build_docker_image(tag="latest"):
    return subprocess.run(
        ["docker", "build", "-t", f"myapp:{tag}", "."],
        capture_output=True, text=True
    )
# 👉 Why useful:
# Prepares container images for deployment in Kubernetes or other platforms.

# ============================================================

# 9. Push Docker image to registry
# Practical use case: Upload image for deployment
def push_docker_image(tag="latest"):
    return subprocess.run(
        ["docker", "push", f"myapp:{tag}"],
        capture_output=True, text=True
    )
# 👉 Why useful:
# Integrates container registry management into CI/CD pipelines.

# ============================================================

# 10. Deploy application using kubectl
# Practical use case: Apply Kubernetes manifests automatically
def deploy_k8s_manifest(file_path):
    return subprocess.run(
        ["kubectl", "apply", "-f", file_path],
        capture_output=True, text=True
    )
# 👉 Why useful:
# Automates deployment steps in Kubernetes clusters.

# ============================================================

# 11. Rollback deployment in Kubernetes
# Practical use case: Undo deployment safely
def rollback_k8s_deployment(deployment_name, namespace="default"):
    return subprocess.run(
        ["kubectl", "rollout", "undo", f"deployment/{deployment_name}", "-n", namespace],
        capture_output=True, text=True
    )
# 👉 Why useful:
# Quickly recover from failed releases in automated pipelines.

# ============================================================

# 12. Notify Slack after pipeline completion
# Practical use case: Send alerts after builds
def notify_slack(webhook_url, message):
    data = {"text": message}
    response = requests.post(webhook_url, json=data)
    return response.status_code
# 👉 Why useful:
# Keeps teams informed automatically about pipeline status.

# ============================================================

# 13. Save pipeline logs
# Practical use case: Persist logs from scripts
def save_pipeline_logs(log_content, filename="pipeline_log.txt"):
    with open(filename, "w") as f:
        f.write(log_content)
    return filename
# 👉 Why useful:
# Allows debugging or auditing of automated pipelines.

# ============================================================

# 14. Generate pipeline report in JSON
# Practical use case: Create structured pipeline report
def generate_pipeline_report(status, duration, triggered_by):
    report = {
        "status": status,
        "duration": duration,
        "triggered_by": triggered_by,
        "timestamp": datetime.utcnow().isoformat()
    }
    with open("pipeline_report.json", "w") as f:
        json.dump(report, f, indent=4)
    return report
# 👉 Why useful:
# Enables automated reporting and integration with dashboards.

# ============================================================

# 15. Run security scan before deployment
# Practical use case: Scan Docker image or code for vulnerabilities
def run_security_scan():
    return subprocess.run(
        ["trivy", "image", "myapp:latest"],
        capture_output=True, text=True
    )
# 👉 Why useful:
# Ensures security checks are part of automated CI/CD pipelines.

# ============================================================
