# ==================================================================
# Practical use cases: AWS automation with Boto3 (AWS SDK) in Python
# ==================================================================


import boto3
from botocore.exceptions import ClientError


# 1. Create an S3 client
# Practical use case: Connect to AWS S3
s3 = boto3.client("s3")
print("S3 client created")
# 👉 Why useful:
# First step to interact with AWS services in scripts and automation.
# ============================================================

# 2. List S3 buckets
# Practical use case: Retrieve all buckets
try:
    response = s3.list_buckets()
    buckets = [b["Name"] for b in response["Buckets"]]
    print("Buckets:", buckets)
except ClientError as e:
    print("Error listing buckets:", e)
# 👉 Why useful:
# Quickly audit S3 resources before deployment or backup tasks.
# ============================================================

# 3. Create S3 bucket
# Practical use case: Automate new bucket creation
bucket_name = "my-devops-bucket-example"
try:
    s3.create_bucket(Bucket=bucket_name)
    print("Bucket created:", bucket_name)
except ClientError as e:
    print("Bucket creation failed:", e)
# 👉 Why useful:
# Automate infrastructure provisioning in CI/CD pipelines.
# ============================================================

# 4. Upload file to S3
# Practical use case: Upload config or artifact
with open("example.txt", "w") as f:
    f.write("DevOps example file")
try:
    s3.upload_file("example.txt", bucket_name, "example.txt")
    print("Uploaded example.txt to S3")
except ClientError as e:
    print("Upload failed:", e)
# 👉 Why useful:
# Store artifacts, logs, or configs in cloud storage automatically.
# ============================================================

# 5. Download file from S3
# Practical use case: Fetch artifact from S3
try:
    s3.download_file(bucket_name, "example.txt", "example_downloaded.txt")
    print("Downloaded example.txt from S3")
except ClientError as e:
    print("Download failed:", e)
# 👉 Why useful:
# Retrieve artifacts for deployment or CI/CD tasks.
# ============================================================

# 6. Delete S3 object
# Practical use case: Cleanup old files
try:
    s3.delete_object(Bucket=bucket_name, Key="example.txt")
    print("Deleted example.txt from S3")
except ClientError as e:
    print("Delete failed:", e)
# 👉 Why useful:
# Automate removal of outdated artifacts or logs.
# ============================================================

# 7. List EC2 instances
# Practical use case: Inventory servers
ec2 = boto3.client("ec2")
try:
    instances = ec2.describe_instances()
    for r in instances["Reservations"]:
        for i in r["Instances"]:
            print("EC2 instance ID:", i["InstanceId"])
except ClientError as e:
    print("Error listing EC2 instances:", e)
# 👉 Why useful:
# Automate monitoring and auditing of cloud infrastructure.
# ============================================================

# 8. Start EC2 instance
# Practical use case: Automate start of servers
instance_id = "i-0123456789abcdef0"
try:
    ec2.start_instances(InstanceIds=[instance_id])
    print(f"Started EC2 instance: {instance_id}")
except ClientError as e:
    print("Start instance failed:", e)
# 👉 Why useful:
# Automate scaling or recovery tasks.
# ============================================================

# 9. Stop EC2 instance
# Practical use case: Automate stop of servers
try:
    ec2.stop_instances(InstanceIds=[instance_id])
    print(f"Stopped EC2 instance: {instance_id}")
except ClientError as e:
    print("Stop instance failed:", e)
# 👉 Why useful:
# Save costs by stopping idle instances automatically.
# ============================================================

# 10. Create IAM user
# Practical use case: Automate user provisioning
iam = boto3.client("iam")
user_name = "devops-user-example"
try:
    iam.create_user(UserName=user_name)
    print("Created IAM user:", user_name)
except ClientError as e:
    print("IAM user creation failed:", e)
# 👉 Why useful:
# Automate user and access management in AWS accounts.
# ============================================================

# 11. Attach policy to IAM user
# Practical use case: Assign permissions
try:
    iam.attach_user_policy(
        UserName=user_name,
        PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
    )
    print("Attached policy to user:", user_name)
except ClientError as e:
    print("Policy attachment failed:", e)
# 👉 Why useful:
# Automate security and permission management for DevOps pipelines.
# ============================================================

# 12. CloudWatch: Put metric data
# Practical use case: Custom monitoring
cloudwatch = boto3.client("cloudwatch")
try:
    cloudwatch.put_metric_data(
        Namespace="DevOpsExample",
        MetricData=[{"MetricName": "DeploymentCount", "Value": 1, "Unit": "Count"}]
    )
    print("Sent metric data to CloudWatch")
except ClientError as e:
    print("CloudWatch metric failed:", e)
# 👉 Why useful:
# Track deployments, SLA, or custom metrics automatically.
# ============================================================

# 13. DynamoDB: Create table
# Practical use case: Provision simple NoSQL DB
dynamodb = boto3.client("dynamodb")
table_name = "DevOpsExampleTable"
try:
    dynamodb.create_table(
        TableName=table_name,
        KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
        ProvisionedThroughput={"ReadCapacityUnits": 1, "WriteCapacityUnits": 1}
    )
    print("Created DynamoDB table:", table_name)
except ClientError as e:
    print("Create table failed:", e)
# 👉 Why useful:
# Automate resource provisioning for small services or CI/CD artifacts.
# ============================================================

# 14. DynamoDB: Put item
# Practical use case: Insert record
try:
    dynamodb.put_item(
        TableName=table_name,
        Item={"id": {"S": "1"}, "name": {"S": "example"}}
    )
    print("Inserted item into table")
except ClientError as e:
    print("Put item failed:", e)
# 👉 Why useful:
# Store deployment info, metadata, or CI/CD tracking automatically.
# ============================================================

# 15. DynamoDB: Get item
# Practical use case: Retrieve record
try:
    resp = dynamodb.get_item(TableName=table_name, Key={"id": {"S": "1"}})
    print("Retrieved item:", resp.get("Item"))
except ClientError as e:
    print("Get item failed:", e)
# 👉 Why useful:
# Fetch deployment or state info for automation scripts.
# ============================================================
