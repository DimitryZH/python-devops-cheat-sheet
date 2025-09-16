# ============================================================
# Practical use cases: Using pathlib in Python for DevOps tasks
# ============================================================


from pathlib import Path


# 1. Path object
# Practical use case: Represent file paths in a clean, cross-platform way
p = Path("logs/app.log")
print("File path:", p)
# 👉 Why useful:
# Avoids manual string concatenation, works on Linux, Windows, macOS.
# ============================================================

# 2. Path.name and Path.suffix
# Practical use case: Extract file name and extension
print("File name:", p.name)
print("File extension:", p.suffix)
# 👉 Why useful:
# Parse filenames for logs, configs, or artifacts.
# ============================================================

# 3. Path.parent
# Practical use case: Get parent directory
print("Parent folder:", p.parent)
# 👉 Why useful:
# Navigate filesystem trees (configs, project dirs).
# ============================================================

# 4. Path.exists()
# Practical use case: Check if file exists before using
print("Does app.log exist?", p.exists())
# 👉 Why useful:
# Avoid errors when reading configs or logs in automation scripts.
# ============================================================

# 5. Path.is_file() / Path.is_dir()
# Practical use case: Differentiate files and directories
print("Is file?", p.is_file())
print("Is directory?", p.is_dir())
# 👉 Why useful:
# Useful for cleanup scripts or deployment validation.
# ============================================================

# 6. Path.mkdir()
# Practical use case: Create directories safely
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)
print("Directory created:", log_dir)
# 👉 Why useful:
# Ensure required folders exist before writing logs or artifacts.
# ============================================================

# 7. Path.write_text() / Path.read_text()
# Practical use case: Write and read config file
config_file = Path("config.yaml")
config_file.write_text("service: api\nreplicas: 2\n")
print("Config content:", config_file.read_text())
# 👉 Why useful:
# Quick way to manage text configs or manifests in automation scripts.
# ============================================================

# 8. Path.iterdir()
# Practical use case: List files in directory
for f in log_dir.iterdir():
    print("File in logs:", f)
# 👉 Why useful:
# Enumerate logs, artifacts, or manifests in a folder.
# ============================================================

# 9. Path.glob()
# Practical use case: Find files matching pattern
for f in Path(".").glob("*.yaml"):
    print("YAML file:", f)
# 👉 Why useful:
# Locate specific manifests or configs in CI/CD pipelines.
# ============================================================

# 10. Path.resolve()
# Practical use case: Get absolute path
print("Absolute path of config.yaml:", config_file.resolve())
# 👉 Why useful:
# Useful in logging and debugging to avoid relative path issues.
# ============================================================

# 11. Path.unlink()
# Practical use case: Delete file safely
tmp_file = Path("temp.txt")
tmp_file.write_text("temporary data")
tmp_file.unlink()
print("temp.txt deleted")
# 👉 Why useful:
# Clean up temporary files in automation or CI/CD jobs.
# ============================================================

# 12. Path.rename()
# Practical use case: Rename log file
log_file = Path("logs/old.log")
log_file.write_text("old log")
log_file.rename("logs/new.log")
print("Renamed old.log -> new.log")
# 👉 Why useful:
# Rotate or rename artifacts/logs during deployments.
# ============================================================

# 13. Path.stat()
# Practical use case: Get file metadata
stat = config_file.stat()
print("File size:", stat.st_size, "bytes")
# 👉 Why useful:
# Check file size, timestamps, permissions before deployments.
# ============================================================

# 14. Path.joinpath()
# Practical use case: Build paths dynamically
artifact_dir = Path("artifacts")
artifact_file = artifact_dir.joinpath("build.tar.gz")
print("Artifact path:", artifact_file)
# 👉 Why useful:
# Safe dynamic path construction instead of string concatenation.
# ============================================================

# 15. Path.rglob()
# Practical use case: Recursively search for files
for f in Path(".").rglob("*.json"):
    print("Found JSON:", f)
# 👉 Why useful:
# Scan project for configs, Terraform states, or secrets.
# ============================================================
