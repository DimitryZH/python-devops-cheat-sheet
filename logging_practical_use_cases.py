# ============================================================
# Practical use cases: Structured logging for DevOps and CI/CD
# ============================================================


import logging


# 1. Basic logging setup
# Practical use case: Replace print() with logging
logging.basicConfig(level=logging.INFO)
logging.info("Application started")
logging.warning("This is a warning")
logging.error("Something went wrong")

# 👉 Why useful:
# Unlike print(), logs can be filtered by level, redirected to files, or external systems.
# ============================================================

# 2. Logging to a file
# Practical use case: Persist logs for CI/CD jobs
logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("Pipeline step 1 completed successfully")
logging.error("Pipeline step 2 failed")

# 👉 Why useful:
# Storing logs helps with troubleshooting failed deployments or SLA reports.
# ============================================================

# 3. Structured logs with context
# Practical use case: Add job IDs, usernames, etc.
logger = logging.getLogger("ci_cd_logger")
handler = logging.StreamHandler()
formatter = logging.Formatter(
    '{"time": "%(asctime)s", "level": "%(levelname)s", "job_id": "%(job_id)s", "message": "%(message)s"}'
)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Adding extra context
extra = {"job_id": "deploy-123"}
logger.info("Deployment started", extra=extra)
logger.error("Deployment failed", extra=extra)

# 👉 Why useful:
# Structured logs (JSON-like) can be parsed by tools like ELK, Splunk, or CloudWatch.
# ============================================================

# 4. Rotating log files
# Practical use case: Avoid huge log files in long-running services
from logging.handlers import RotatingFileHandler

rotating_handler = RotatingFileHandler("service.log", maxBytes=200, backupCount=3)
rotating_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
rotating_logger = logging.getLogger("service")
rotating_logger.addHandler(rotating_handler)
rotating_logger.setLevel(logging.INFO)

for i in range(20):
    rotating_logger.info("Processing request %d", i)

# 👉 Why useful:
# Prevents logs from consuming too much disk space in production environments.
# ============================================================

# 5. Syslog integration
# Practical use case: Send logs to a centralized syslog server
try:
    from logging.handlers import SysLogHandler
    syslog_logger = logging.getLogger("syslog_example")
    syslog_logger.setLevel(logging.INFO)
    syslog_handler = SysLogHandler(address="/dev/log")
    syslog_logger.addHandler(syslog_handler)
    syslog_logger.info("Syslog integration test")
except Exception as e:
    print("Syslog not available on this system:", e)

# 👉 Why useful:
# Centralized logging is critical for monitoring clusters, especially in Kubernetes or cloud setups.
# ============================================================
