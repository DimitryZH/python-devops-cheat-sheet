# ============================================================
# Practical use cases: Using subprocess module in DevOps
# ============================================================

import subprocess


# 1. subprocess.run()
# Practical use case: Run a simple shell command
result = subprocess.run(["echo", "Hello from subprocess"], capture_output=True, text=True)
print("Output:", result.stdout.strip())
# 👉 Why useful:
# Preferred way to execute commands in automation scripts.
# ============================================================

# 2. subprocess.run() with error handling
# Practical use case: Run command and check if it failed
try:
    subprocess.run(["ls", "/nonexistent"], check=True)
except subprocess.CalledProcessError as e:
    print("Command failed:", e)
# 👉 Why useful:
# Ensures CI/CD fails early if a command breaks.
# ============================================================

# 3. subprocess.check_output()
# Practical use case: Capture command output directly
output = subprocess.check_output(["date"], text=True)
print("Current date:", output.strip())
# 👉 Why useful:
# Handy when script needs command results as variables.
# ============================================================

# 4. subprocess.Popen()
# Practical use case: Run command asynchronously
process = subprocess.Popen(["sleep", "2"])
print("Started background process (sleep 2)")
process.wait()
print("Background process finished")
# 👉 Why useful:
# Useful for running long tasks while continuing other operations.
# ============================================================

# 5. subprocess.run() with shell=True
# Practical use case: Run a command with pipes
cmd = "echo 'devops' | tr 'a-z' 'A-Z'"
result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
print("Uppercased:", result.stdout.strip())
# 👉 Why useful:
# Allows using shell pipelines in scripts.
# ============================================================

# 6. subprocess.run() with environment variables
# Practical use case: Run command with custom env
custom_env = {"MY_VAR": "123"}
result = subprocess.run(["bash", "-c", "echo $MY_VAR"], capture_output=True, text=True, env=custom_env)
print("MY_VAR from env:", result.stdout.strip())
# 👉 Why useful:
# Lets you test or override env vars in deployments.
# ============================================================

# 7. subprocess.run() redirecting output to file
# Practical use case: Save logs
with open("subprocess_log.txt", "w") as f:
    subprocess.run(["echo", "Log entry created"], stdout=f)
print("Log file written: subprocess_log.txt")
# 👉 Why useful:
# Helps redirect logs into files during automation.
# ============================================================

# 8. subprocess.run() with input
# Practical use case: Provide input to a command
result = subprocess.run(["cat"], input="Hello Input\n", capture_output=True, text=True)
print("Cat command received:", result.stdout.strip())
# 👉 Why useful:
# Useful for simulating interactive commands.
# ============================================================

# 9. subprocess.PIPE
# Practical use case: Chain commands (producer -> consumer)
p1 = subprocess.Popen(["echo", "cloud engineering"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["tr", "a-z", "A-Z"], stdin=p1.stdout, stdout=subprocess.PIPE, text=True)
p1.stdout.close()  # Allow p1 to receive SIGPIPE if p2 exits
output = p2.communicate()[0]
print("Chained output:", output.strip())
# 👉 Why useful:
# Simulates Unix-style piping between commands in Python.
# ============================================================

# 10. subprocess.run() with timeout
# Practical use case: Kill long-running commands
try:
    subprocess.run(["sleep", "10"], timeout=3)
except subprocess.TimeoutExpired:
    print("Command timed out")
# 👉 Why useful:
# Prevents scripts from hanging indefinitely.
# ============================================================

# 11. subprocess.run() cross-platform command
# Practical use case: Print system info (works on Linux/macOS/Windows)
cmd = ["uname", "-a"] if subprocess.run(["uname"], capture_output=True).returncode == 0 else ["ver"]
result = subprocess.run(cmd, capture_output=True, text=True)
print("System info:", result.stdout.strip())
# 👉 Why useful:
# Great for gathering system info in deployment scripts.
# ============================================================

# 12. subprocess.run() return code
# Practical use case: Check deployment status
cmd = ["ls", "."]
result = subprocess.run(cmd)
print("Return code:", result.returncode)
# 👉 Why useful:
# Return codes decide success/failure in CI/CD jobs.
# ============================================================
