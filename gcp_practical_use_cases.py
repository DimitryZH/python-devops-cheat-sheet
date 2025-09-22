# ============================================================
# Practical use cases: GCP automation with Python SDK
# ============================================================

from google.cloud import storage, compute_v1
from google.oauth2 import service_account
import google.api_core.exceptions

# 1. Authenticate with GCP
# Practical use case: Use service account credentials
try:
    credentials = service_account.Credentials.from_service_account_file(
        "service-account.json"
    )
    print("GCP authentication successful")
except Exception as e:
    print("Authentication failed:", e)
# 👉 Why useful:
# Required first step for any GCP automation script.
# ============================================================

# 2. Initialize Storage client
# Practical use case: Work with GCS buckets
try:
    storage_client = storage.Client(credentials=credentials)
    print("Storage client initialized")
except Exception as e:
    print("Failed to initialize storage client:", e)
# 👉 Why useful:
# Access Google Cloud Storage for logs, configs, and artifacts.
# ============================================================

# 3. List buckets
# Practical use case: Inventory storage buckets
try:
    buckets = list(storage_client.list_buckets())
    print("Buckets:", [b.name for b in buckets])
except google.api_core.exceptions.GoogleAPIError as e:
    print("Failed to list buckets:", e)
# 👉 Why useful:
# Auditing and validating GCS resources for DevOps.
# ============================================================

# 4. Create a bucket
# Practical use case: Automate storage provisioning
bucket_name = "devops-example-bucket"
try:
    bucket = storage_client.bucket(bucket_name)
    bucket.location = "US"
    storage_client.create_bucket(bucket)
    print("Bucket created:", bucket.name)
except Exception as e:
    print("Bucket creation failed:", e)
# 👉 Why useful:
# Automated artifact storage setup in CI/CD workflows.
# ============================================================

# 5. Upload file to bucket
# Practical use case: Push build artifact to GCS
try:
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob("example.txt")
    blob.upload_from_filename("example.txt")
    print("File uploaded to bucket")
except Exception as e:
    print("Upload failed:", e)
# 👉 Why useful:
# Store build outputs, logs, or configs in GCS during pipelines.
# ============================================================

# 6. Download file from bucket
# Practical use case: Retrieve artifacts from GCS
try:
    blob.download_to_filename("downloaded_example.txt")
    print("File downloaded successfully")
except Exception as e:
    print("Download failed:", e)
# 👉 Why useful:
# Pull stored artifacts back into automation scripts or test jobs.
# ============================================================

# 7. Initialize Compute Engine client
# Practical use case: Manage VM instances
try:
    compute_client = compute_v1.InstancesClient(credentials=credentials)
    print("Compute client initialized")
except Exception as e:
    print("Failed to init compute client:", e)
# 👉 Why useful:
# VM lifecycle management is key in infrastructure automation.
# ============================================================

# 8. List VM instances
# Practical use case: Inventory running workloads
project = "<YOUR_PROJECT_ID>"
zone = "us-central1-a"
try:
    result = compute_client.list(project=project, zone=zone)
    print("VMs:", [i.name for i in result])
except Exception as e:
    print("Failed to list VMs:", e)
# 👉 Why useful:
# Monitoring infrastructure state from Python scripts.
# ============================================================

# 9. Start a VM
# Practical use case: Automate VM lifecycle
instance_name = "<YOUR_INSTANCE>"
try:
    operation = compute_client.start(project=project, zone=zone, instance=instance_name)
    print("Start VM operation:", operation)
except Exception as e:
    print("VM start failed:", e)
# 👉 Why useful:
# Reduce costs by automating start/stop of VMs.
# ============================================================

# 10. Stop a VM
# Practical use case: Shut down compute instances
try:
    operation = compute_client.stop(project=project, zone=zone, instance=instance_name)
    print("Stop VM operation:", operation)
except Exception as e:
    print("VM stop failed:", e)
# 👉 Why useful:
# Automate shutdown during off-hours to save money.
# ============================================================

# 11. Create a firewall rule
# Practical use case: Secure workloads programmatically
from google.cloud import compute_v1

fw_client = compute_v1.FirewallsClient(credentials=credentials)
firewall_rule = compute_v1.Firewall(
    name="allow-ssh",
    direction="INGRESS",
    allowed=[compute_v1.Allowed(IPProtocol="tcp", ports=["22"])],
    source_ranges=["0.0.0.0/0"],
    network="global/networks/default",
)
try:
    op = fw_client.insert(project=project, firewall_resource=firewall_rule)
    print("Firewall rule created:", op)
except Exception as e:
    print("Firewall rule creation failed:", e)
# 👉 Why useful:
# Automate network security as part of infrastructure code.
# ============================================================

# 12. Handle GCP errors gracefully
# Practical use case: Use exception handling for resilience
try:
    non_existing = storage_client.get_bucket("non-existent-bucket")
except google.api_core.exceptions.NotFound:
    print("Bucket not found (handled gracefully)")
# 👉 Why useful:
# Prevent automation scripts from crashing due to missing resources.
# ============================================================

# 13. Service account impersonation
# Practical use case: Work with multiple service accounts
try:
    impersonated_creds = credentials.with_subject("other-service-account@project.iam.gserviceaccount.com")
    print("Impersonated credentials created")
except Exception as e:
    print("Impersonation failed:", e)
# 👉 Why useful:
# Enables cross-project automation with least privilege access.
# ============================================================

# 14. Automate infrastructure audit
# Practical use case: Validate resource compliance
try:
    for bucket in storage_client.list_buckets():
        print(f"Bucket {bucket.name}, location: {bucket.location}")
except Exception as e:
    print("Audit failed:", e)
# 👉 Why useful:
# Regular compliance audits are core DevOps responsibilities.
# ============================================================

# 15. Clean up resources
# Practical use case: Tear down test infrastructure   
try:
    bucket = storage_client.bucket(bucket_name)
    bucket.delete(force=True)
    print("Bucket deleted:", bucket_name)
except Exception as e:
    print("Bucket deletion failed:", e)
# 👉 Why useful:
# Avoid unnecessary costs by cleaning up test/dev resources.
# ============================================================
