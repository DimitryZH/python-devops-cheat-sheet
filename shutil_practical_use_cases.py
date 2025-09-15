# ============================================================
# Practical use cases: Using shutil module in DevOps
# ============================================================


import shutil
from pathlib import Path


# 1. shutil.copy()
# Practical use case: Copy config file to backup location
Path("config.yaml").write_text("service: api\nreplicas: 3\n")
shutil.copy("config.yaml", "config_backup.yaml")
print("Copied config.yaml -> config_backup.yaml")
# 👉 Why useful:
# Backup configs before deployments or edits.
# ============================================================

# 2. shutil.copy2()
# Practical use case: Preserve metadata while copying
shutil.copy2("config.yaml", "config_with_meta.yaml")
print("Copied with metadata preserved")
# 👉 Why useful:
# Keeps timestamps and permissions (important in prod systems).
# ============================================================

# 3. shutil.move()
# Practical use case: Move logs to archive folder
Path("logs").mkdir(exist_ok=True)
Path("app.log").write_text("Log entry\n")
shutil.move("app.log", "logs/app.log")
print("Moved app.log -> logs/")
# 👉 Why useful:
# Archive old logs or artifacts.
# ============================================================

# 4. shutil.rmtree()
# Practical use case: Remove temporary directory
Path("temp_dir").mkdir(exist_ok=True)
(Path("temp_dir") / "temp.txt").write_text("Temporary data")
shutil.rmtree("temp_dir")
print("Removed temp_dir")
# 👉 Why useful:
# Clean up build directories after CI/CD runs.
# ============================================================

# 5. shutil.make_archive()
# Practical use case: Create archive of deployment package
Path("release").mkdir(exist_ok=True)
(Path("release") / "app.py").write_text("print('App running')")
archive_path = shutil.make_archive("release_package", "zip", "release")
print("Created archive:", archive_path)
# 👉 Why useful:
# Package code/artifacts for deployment or distribution.
# ============================================================

# 6. shutil.unpack_archive()
# Practical use case: Extract archive
shutil.unpack_archive("release_package.zip", "release_extracted")
print("Extracted release_package.zip -> release_extracted/")
# 👉 Why useful:
# Automate unpacking artifacts from CI/CD.
# ============================================================

# 7. shutil.disk_usage()
# Practical use case: Check free space before deployment
usage = shutil.disk_usage(".")
print("Disk total:", usage.total, "bytes")
print("Disk free:", usage.free, "bytes")
# 👉 Why useful:
# Ensure enough disk space before deploying containers or logs.
# ============================================================

# 8. shutil.which()
# Practical use case: Verify CLI tool availability
kubectl_path = shutil.which("kubectl")
print("kubectl found at:", kubectl_path if kubectl_path else "not installed")
# 👉 Why useful:
# Check required tools (kubectl, terraform, ansible) before running scripts.
# ============================================================

# 9. shutil.copytree()
# Practical use case: Duplicate directory structure
Path("project").mkdir(exist_ok=True)
(Path("project") / "main.py").write_text("print('hello')")
shutil.copytree("project", "project_copy", dirs_exist_ok=True)
print("Copied project -> project_copy")
# 👉 Why useful:
# Duplicate project environments or configs for testing.
# ============================================================

# 10. shutil.get_terminal_size()
# Practical use case: Adjust script output formatting
size = shutil.get_terminal_size()
print(f"Terminal size: {size.columns}x{size.lines}")
# 👉 Why useful:
# Adjust logging or progress bars for better readability in CI/CD logs.
# ============================================================
