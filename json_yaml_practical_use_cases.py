# ============================================================
# Practical use cases: Using JSON and YAML in DevOps
# ============================================================


import json
from pathlib import Path


# 1. json.loads()
# Practical use case: Parse JSON from API response
json_data = '{"service": "api", "replicas": 3}'
parsed = json.loads(json_data)
print("Parsed JSON:", parsed)
# 👉 Why useful:
# APIs (AWS, Azure, Kubernetes) return JSON responses that must be parsed.
# ============================================================

# 2. json.dumps()
# Practical use case: Convert Python dict to JSON string
config = {"service": "worker", "replicas": 2}
json_string = json.dumps(config, indent=2)
print("JSON string:\n", json_string)
# 👉 Why useful:
# Serialize configs or payloads for APIs and tools.
# ============================================================

# 3. json.load()
# Practical use case: Read JSON config from file
Path("config.json").write_text('{"version": "1.0", "debug": true}')
with open("config.json") as f:
    data = json.load(f)
print("Config loaded:", data)
# 👉 Why useful:
# Store infrastructure or pipeline configs in JSON files.
# ============================================================

# 4. json.dump()
# Practical use case: Save Python dict to JSON file
settings = {"env": "prod", "region": "us-east-1"}
with open("settings.json", "w") as f:
    json.dump(settings, f, indent=2)
print("Saved settings.json")
# 👉 Why useful:
# Persist CI/CD or IaC settings in JSON format.
# ============================================================

# 5. json for Terraform/CloudFormation
# Practical use case: Modify IaC templates
tf_state = {"resources": [{"name": "app", "type": "aws_instance"}]}
with open("terraform_state.json", "w") as f:
    json.dump(tf_state, f, indent=2)
print("Terraform state example saved")
# 👉 Why useful:
# Automate edits/validations of Terraform or CloudFormation states.
# ============================================================

# 6. import yaml (requires PyYAML)
# Practical use case: Parse Kubernetes manifest
try:
    import yaml
    yaml_data = """
    apiVersion: v1
    kind: Pod
    metadata:
      name: myapp
    spec:
      containers:
        - name: app
          image: nginx
    """
    parsed_yaml = yaml.safe_load(yaml_data)
    print("Parsed YAML:", parsed_yaml)
except ImportError:
    print("PyYAML not installed, skipping YAML examples")
# 👉 Why useful:
# Kubernetes, Ansible, and CI/CD configs use YAML format.
# ============================================================

# 7. yaml.safe_load_all()
# Practical use case: Parse multi-document YAML (K8s manifests)
try:
    multi_yaml = """
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: cm1
    ---
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: cm2
    """
    for doc in yaml.safe_load_all(multi_yaml):
        print("YAML doc:", doc)
except NameError:
    pass
# 👉 Why useful:
# Handle multiple Kubernetes resources in one YAML file.
# ============================================================

# 8. yaml.dump()
# Practical use case: Generate YAML config from Python dict
try:
    deployment = {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {"name": "myapp"},
        "spec": {"replicas": 2}
    }
    yaml_string = yaml.dump(deployment, sort_keys=False)
    print("YAML output:\n", yaml_string)
except NameError:
    pass
# 👉 Why useful:
# Automate manifest generation for Kubernetes or Ansible.
# ============================================================

# 9. yaml.safe_dump()
# Practical use case: Save YAML config to file
try:
    service = {
        "apiVersion": "v1",
        "kind": "Service",
        "metadata": {"name": "my-service"}
    }
    with open("service.yaml", "w") as f:
        yaml.safe_dump(service, f, sort_keys=False)
    print("Saved service.yaml")
except NameError:
    pass
# 👉 Why useful:
# Store IaC configs or CI/CD manifests in YAML.
# ============================================================

# 10. YAML + JSON conversion
# Practical use case: Convert JSON to YAML (and back)
try:
    json_text = '{"app": "backend", "replicas": 3}'
    obj = json.loads(json_text)
    yaml_text = yaml.dump(obj, sort_keys=False)
    print("Converted JSON -> YAML:\n", yaml_text)
except NameError:
    pass
# 👉 Why useful:
# Interoperate between tools that use JSON (Terraform, APIs)
# and YAML (Kubernetes, Ansible).
# ============================================================
