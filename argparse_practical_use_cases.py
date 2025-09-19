# ============================================================
# Practical use cases: CLI tools for DevOps with argparse
# ============================================================


import argparse


# 1. Basic CLI parser
# Practical use case: Build DevOps helper scripts with arguments
parser = argparse.ArgumentParser(description="DevOps helper CLI")
parser.add_argument("--env", help="Target environment", default="dev")
args = parser.parse_args()

print(f"Deploying to environment: {args.env}")

# 👉 Why useful:
# Makes scripts flexible across environments (dev/staging/prod) in CI/CD pipelines.
# ============================================================

# 2. Multiple arguments
# Practical use case: Control behavior of automation tools
parser = argparse.ArgumentParser(description="Backup utility")
parser.add_argument("--source", required=True, help="Source folder")
parser.add_argument("--dest", required=True, help="Destination folder")
parser.add_argument("--compress", action="store_true", help="Enable compression")
args = parser.parse_args()

print(f"Backing up {args.source} to {args.dest}, compress={args.compress}")

# 👉 Why useful:
# Allows DevOps engineers to re-use the same script for different jobs with flags.
# ============================================================

# 3. Subcommands
# Practical use case: Multi-function CLI (deploy, rollback)
parser = argparse.ArgumentParser(description="CI/CD Deployment CLI")
subparsers = parser.add_subparsers(dest="command")

deploy = subparsers.add_parser("deploy", help="Deploy application")
deploy.add_argument("--version", required=True, help="App version to deploy")

rollback = subparsers.add_parser("rollback", help="Rollback deployment")
rollback.add_argument("--id", required=True, help="Deployment ID")

args = parser.parse_args()

if args.command == "deploy":
    print(f"Deploying version {args.version}")
elif args.command == "rollback":
    print(f"Rolling back deployment {args.id}")

# 👉 Why useful:
# A single CLI tool can handle multiple DevOps workflows like deploy, rollback, scale, etc.
# ============================================================

# 4. Argument types and validation
# Practical use case: Ensure correct input types for scripts
parser = argparse.ArgumentParser(description="Scale application")
parser.add_argument("--replicas", type=int, required=True, help="Number of replicas")
args = parser.parse_args()

print(f"Scaling application to {args.replicas} replicas")

# 👉 Why useful 
# Prevents runtime errors by validating input types (int, float, file paths).
# ============================================================
# 5. Help and usage messages
# Practical use case: Self-documenting CLI tools
# Run `python script.py --help` to see usage
parser = argparse.ArgumentParser(description="Monitor service status")  
parser.add_argument("--url", required=True, help="Service URL to monitor")
args = parser.parse_args()

print(f"Monitoring service at {args.url}")

# 👉 Why useful: 
# Built-in help makes it easy for team members to understand and use scripts without external docs.
# ============================================================
# 6. Default values
# Practical use case: Sensible defaults for common parameters  
# Run `python script.py --help` to see usage
parser = argparse.ArgumentParser(description="Log rotation utility")
parser.add_argument("--logfile", default="/var/log/app.log", help="Log file to rotate")
parser.add_argument("--max-size", type=int, default=100, help="Max log size in MB")
args = parser.parse_args()    
print(f"Rotating {args.logfile} with max size {args.max_size}MB")
# 👉 Why useful:
# Provides convenience for common use cases while allowing overrides.
# ============================================================
# 7. Environment variable integration
# Practical use case: Override CLI args with env vars in CI/CD
# Run `python script.py --help` to see usage
import os   
parser = argparse.ArgumentParser(description="Database migration tool")
parser.add_argument("--db-url", default=os.getenv("DB_URL"), help="Database connection URL")
args = parser.parse_args()    
print(f"Migrating database to {args.db_url}")
# 👉 Why useful
# Supports 12-factor app principles by allowing configuration via environment variables.
# ============================================================
# 8. Custom error handling
# Practical use case: Friendly error messages for users
# Run `python script.py --help` to see usage
# This will raise an error if --port is not an integer
parser = argparse.ArgumentParser(description="Start web server")  
parser.add_argument("--port", type=int, required=True, help="Port number to listen on")
args = parser.parse_args()    
print(f"Starting server on port {args.port}")
# 👉 Why useful
# Improves user experience by providing clear feedback on incorrect usage.
# ============================================================
# 9. Argument groups
# Practical use case: Organize related parameters in complex CLIs
# Run `python script.py --help` to see usage
parser = argparse.ArgumentParser(description="Complex DevOps tool")
auth_group = parser.add_argument_group("Authentication") 
auth_group.add_argument("--user", help="Username")
auth_group.add_argument("--password", help="Password")
args = parser.parse_args()    
print(f"User: {args.user}, Password: {'*' * len(args.password) if args.password else None}")
# 👉 Why useful
# Improves readability of help messages by grouping related options.
# ============================================================
# 10. Version flag
# Practical use case: Display script version
# Run `python script.py --help` to see usage
parser = argparse.ArgumentParser(description="Versioned CLI tool")
parser.add_argument("--version", action="version", version="%(prog)s 1.0")
args = parser.parse_args()    
print("This is a versioned CLI tool")  
# 👉 Why useful   
# Allows users to quickly check the version of the tool they are using.
# ============================================================
