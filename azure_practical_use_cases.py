# ============================================================
# Practical use cases: Azure automation with Python SDK
# ============================================================

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.core.exceptions import AzureError

# 1. Authenticate to Azure
# Practical use case: Connect to Azure using DefaultAzureCredential
try:
    credential = DefaultAzureCredential()
    print("Azure authentication successful")
except AzureError as e:
    print("Authentication failed:", e)
# 👉 Why useful:
# Required first step for any Azure automation script.
# ============================================================

# 2. Resource management client
# Practical use case: Create client for managing resources
subscription_id = "<YOUR_SUBSCRIPTION_ID>"
resource_client = ResourceManagementClient(credential, subscription_id)
print("ResourceManagementClient created")
# 👉 Why useful:
# Manage resource groups, deployments, and Azure resources programmatically.
# ============================================================

# 3. Create a resource group
# Practical use case: Automate resource group provisioning
rg_name = "DevOpsExampleRG"
location = "eastus"
try:
    rg_result = resource_client.resource_groups.create_or_update(
        rg_name, {"location": location}
    )
    print("Resource group created:", rg_result.name)
except AzureError as e:
    print("Resource group creation failed:", e)
# 👉 Why useful:
# Automate infrastructure provisioning for DevOps pipelines.
# ============================================================

# 4. List resource groups
# Practical use case: Inventory
try:
    for rg in resource_client.resource_groups.list():
        print("Resource group:", rg.name)
except AzureError as e:
    print("List resource groups failed:", e)
# 👉 Why useful:
# Quick audit of your environment before deployments.
# ============================================================

# 5. Compute client
# Practical use case: Manage virtual machines
compute_client = ComputeManagementClient(credential, subscription_id)
print("ComputeManagementClient created")
# 👉 Why useful:
# Automate VM lifecycle for deployments or testing environments.
# ============================================================

# 6. List VMs in a resource group
# Practical use case: Inventory VMs
try:
    for vm in compute_client.virtual_machines.list(rg_name):
        print("VM name:", vm.name)
except AzureError as e:
    print("List VMs failed:", e)
# 👉 Why useful:
# Track running VMs and automate monitoring.
# ============================================================

# 7. Start VM
# Practical use case: Start virtual machine
vm_name = "devops-vm-example"
try:
    async_vm_start = compute_client.virtual_machines.begin_start(rg_name, vm_name)
    async_vm_start.wait()
    print(f"VM {vm_name} started")
except AzureError as e:
    print("Start VM failed:", e)
# 👉 Why useful:
# Automate scaling or testing environments in DevOps pipelines.
# ============================================================

# 8. Stop VM
# Practical use case: Stop virtual machine
try:
    async_vm_stop = compute_client.virtual_machines.begin_power_off(rg_name, vm_name)
    async_vm_stop.wait()
    print(f"VM {vm_name} stopped")
except AzureError as e:
    print("Stop VM failed:", e)
# 👉 Why useful:
# Save costs by stopping idle VMs automatically.
# ============================================================

# 9. Storage client
# Practical use case: Manage Azure Storage accounts
storage_client = StorageManagementClient(credential, subscription_id)
print("StorageManagementClient created")
# 👉 Why useful:
# Automate blob storage for logs, artifacts, or backups.
# ============================================================

# 10. Create storage account
# Practical use case: Provision storage
storage_account_name = "devopsstorageexample"
try:
    storage_async = storage_client.storage_accounts.begin_create(
        rg_name,
        storage_account_name,
        {
            "sku": {"name": "Standard_LRS"},
            "kind": "StorageV2",
            "location": location,
        },
    )
    storage_account = storage_async.result()
    print("Storage account created:", storage_account.name)
except AzureError as e:
    print("Storage account creation failed:", e)
# 👉 Why useful:
# Automate infrastructure needed for artifacts or backups.
# ============================================================

# 11. List storage accounts
# Practical use case: Inventory storage
try:
    for sa in storage_client.storage_accounts.list_by_resource_group(rg_name):
        print("Storage account:", sa.name)
except AzureError as e:
    print("List storage accounts failed:", e)
# 👉 Why useful:
# Quickly audit storage resources for maintenance or cleanup.
# ============================================================

# 12. Delete resource group
# Practical use case: Cleanup environment
try:
    async_rg_delete = resource_client.resource_groups.begin_delete(rg_name)
    async_rg_delete.wait()
    print("Deleted resource group:", rg_name)
except AzureError as e:
    print("Delete resource group failed:", e)
# 👉 Why useful:
# Automate cleanup of dev/test resources to save costs.
# ============================================================

# 13. Tag resource group
# Practical use case: Organize resources
try:
    rg_update = resource_client.resource_groups.update(
        rg_name,
        {"tags": {"Environment": "DevOps", "Owner": "DevTeam"}},
    )
    print("Resource group tags updated:", rg_update.tags)
except AzureError as e:
    print("Update tags failed:", e)
# 👉 Why useful:
# Track and organize resources for billing, auditing, or governance.
# ============================================================

# 14. Deploy ARM template
# Practical use case: Automated infrastructure deployment
template = {
    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
    "contentVersion": "1.0.0.0",
    "resources": []
}
parameters = {}
try:
    deployment = resource_client.deployments.begin_create_or_update(
        rg_name,
        "DevOpsExampleDeployment",
        {"properties": {"template": template, "parameters": parameters, "mode": "Incremental"}},
    )
    deployment.result()
    print("ARM template deployed")
except AzureError as e:
    print("Deployment failed:", e)
# 👉 Why useful:
# Automate repeatable infrastructure provisioning in CI/CD pipelines.
# ============================================================

# 15. Get resource group details
# Practical use case: Inspect environment
try:
    rg = resource_client.resource_groups.get(rg_name)
    print("Resource group location:", rg.location)
    print("Resource group tags:", rg.tags)
except AzureError as e:
    print("Get resource group details failed:", e)
# 👉 Why useful:
# Retrieve metadata for automation scripts and monitoring dashboards.
# ============================================================
# 16. List all resources in a resource group
# Practical use case: Inventory resources
try:
    for resource in resource_client.resources.list_by_resource_group(rg_name):
        print("Resource:", resource.name, "Type:", resource.type)
except AzureError as e:
    print("List resources failed:", e)
# 👉 Why useful
# Comprehensive view of all resources for auditing and cleanup.
# ============================================================
# 17. Update VM size
# Practical use case: Scale VM
try:
    vm = compute_client.virtual_machines.get(rg_name, vm_name)
    vm.hardware_profile.vm_size = "Standard_DS2_v2"
    async_vm_update = compute_client.virtual_machines.begin_create_or_update(rg_name, vm_name, vm)
    async_vm_update.wait()
    print(f"VM {vm_name} resized")
except AzureError as e:
    print("Resize VM failed:", e)
# 👉 Why useful
# Automate scaling of VMs based on workload demands.
# ============================================================
