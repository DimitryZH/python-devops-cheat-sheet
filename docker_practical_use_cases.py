# ============================================================
# Practical DevOps examples with Docker (docker-py + docker CLI fallback)
# ============================================================

import json
import shutil
import subprocess
import tempfile
import time
from pathlib import Path

# Try to import docker SDK; fall back to CLI where appropriate
try:
    import docker
    docker_client = docker.from_env()
except Exception:
    docker = None
    docker_client = None

# Helper: check whether docker CLI exists
DOCKER_CLI = shutil.which("docker") is not None
# ============================================================


# 1. Check Docker daemon availability
# Practical use case: Ensure Docker is running before CI/CD steps
if docker_client:
    try:
        docker_client.ping()
        print("Docker SDK: daemon reachable")
    except Exception as e:
        print("Docker SDK ping failed:", e)
elif DOCKER_CLI:
    try:
        subprocess.run(["docker", "version"], check=True, capture_output=True, text=True)
        print("Docker CLI: daemon reachable")
    except Exception as e:
        print("Docker CLI check failed:", e)
else:
    print("Docker not available (no SDK and no CLI).")
# 👉 Why useful:
# Before running builds or container tasks in pipelines, validate Docker is available.
# ============================================================


# 2. List local images
# Practical use case: Inventory images on the build agent
if docker_client:
    images = docker_client.images.list()
    print("Images (SDK):", [f"{i.tags} ({i.short_id})" for i in images])
elif DOCKER_CLI:
    out = subprocess.check_output(["docker", "images", "--format", "{{.Repository}}:{{.Tag}} {{.ID}}"], text=True)
    print("Images (CLI):")
    print(out.strip())
# 👉 Why useful:
# Know which images are cached locally to speed up CI/CD and avoid unnecessary pulls.
# ============================================================


# 3. Pull an image
# Practical use case: Ensure required base images exist before build
image_name = "nginx:latest"
if docker_client:
    try:
        img = docker_client.images.pull(image_name)
        print("Pulled (SDK):", image_name, "->", img.short_id)
    except Exception as e:
        print("Pull failed (SDK):", e)
elif DOCKER_CLI:
    try:
        subprocess.run(["docker", "pull", image_name], check=True)
        print("Pulled (CLI):", image_name)
    except Exception as e:
        print("Pull failed (CLI):", e)
# 👉 Why useful:
# Pre-pulling images avoids slowdowns during deployment and ensures determinism.
# ============================================================


# 4. Build an image from a simple Dockerfile
# Practical use case: Build a lightweight image for tests
dockerfile_dir = Path(tempfile.mkdtemp(prefix="docker-build-"))
(dockerfile_dir / "Dockerfile").write_text("""\
FROM alpine:3.17
RUN echo "hello from built image" > /hello.txt
""")
image_tag = "devops/example:latest"
if docker_client:
    try:
        image, logs = docker_client.images.build(path=str(dockerfile_dir), tag=image_tag)
        print("Built (SDK):", image_tag, "->", image.short_id)
    except Exception as e:
        print("Build failed (SDK):", e)
elif DOCKER_CLI:
    try:
        subprocess.run(["docker", "build", "-t", image_tag, str(dockerfile_dir)], check=True)
        print("Built (CLI):", image_tag)
    except Exception as e:
        print("Build failed (CLI):", e)
# 👉 Why useful:
# Automate image creation in CI for integration tests or packaging.
# ============================================================


# 5. Run a container (detached) and inspect its status
# Practical use case: Launch a service container for integration tests
container_name = "devops_example_runner"
if docker_client:
    try:
        # Remove existing with same name if present
        try:
            old = docker_client.containers.get(container_name)
            old.remove(force=True)
        except Exception:
            pass
        container = docker_client.containers.run("nginx:latest", name=container_name, detach=True, ports={"80/tcp": None})
        print("Started container (SDK):", container.name, container.short_id)
        container.reload()
        print("Container status:", container.status)
    except Exception as e:
        print("Run failed (SDK):", e)
elif DOCKER_CLI:
    try:
        subprocess.run(["docker", "run", "-d", "--name", container_name, "nginx:latest"], check=True)
        out = subprocess.check_output(["docker", "ps", "--filter", f"name={container_name}", "--format", "{{.Names}} {{.Status}}"], text=True)
        print("Started container (CLI):", out.strip())
    except Exception as e:
        print("Run failed (CLI):", e)
# 👉 Why useful:
# Spawn containers dynamically in pipelines for tests, smoke checks, or ephemeral services.
# ============================================================


# 6. Execute a command inside a running container
# Practical use case: Run ad-hoc commands to collect diagnostics
if docker_client:
    try:
        c = docker_client.containers.get(container_name)
        exec_result = c.exec_run(["/bin/sh", "-c", "cat /hello.txt || echo nofile"], demux=True)
        out = exec_result.output if hasattr(exec_result, "output") else exec_result[1]
        print("Exec output (SDK):", out)
    except Exception as e:
        print("Exec failed (SDK):", e)
elif DOCKER_CLI:
    try:
        out = subprocess.check_output(["docker", "exec", container_name, "sh", "-c", "cat /hello.txt || echo nofile"], text=True)
        print("Exec output (CLI):", out.strip())
    except Exception as e:
        print("Exec failed (CLI):", e)
# 👉 Why useful:
# Helpful to gather files, check configs, or run quick health commands inside containers.
# ============================================================


# 7. Stream container logs
# Practical use case: Attach to logs for troubleshooting
if docker_client:
    try:
        c = docker_client.containers.get(container_name)
        print("Last 5 log lines (SDK):")
        for line in c.logs(tail=5).splitlines():
            print(line.decode() if isinstance(line, bytes) else line)
    except Exception as e:
        print("Logs failed (SDK):", e)
elif DOCKER_CLI:
    try:
        out = subprocess.check_output(["docker", "logs", "--tail", "5", container_name], text=True)
        print("Last 5 log lines (CLI):")
        print(out.strip())
    except Exception as e:
        print("Logs failed (CLI):", e)
# 👉 Why useful:
# Quickly inspect runtime logs in automation or during incident response.
# ============================================================


# 8. Stop and remove a container
# Practical use case: Clean up test containers after use
if docker_client:
    try:
        c = docker_client.containers.get(container_name)
        c.stop(timeout=5)
        c.remove()
        print("Stopped and removed container (SDK):", container_name)
    except Exception as e:
        print("Stop/remove failed (SDK):", e)
elif DOCKER_CLI:
    try:
        subprocess.run(["docker", "rm", "-f", container_name], check=True)
        print("Stopped and removed container (CLI):", container_name)
    except Exception as e:
        print("Stop/remove failed (CLI):", e)
# 👉 Why useful:
# Prevent resource leaks on build agents; ensure idempotent pipelines.
# ============================================================


# 9. Tag and (optionally) push an image to registry
# Practical use case: Prepare and push CI-built artifacts
local_tag = "devops/example:ci"
remote_tag = "registry.example.com/devops/example:ci"
if docker_client:
    try:
        image = docker_client.images.get(image_tag)
        image.tag(remote_tag)
        print("Tagged image (SDK):", remote_tag)
        # Push may require auth; demonstrate but catch errors
        try:
            push_log = docker_client.images.push(remote_tag)
            print("Push output (SDK):", push_log[:200])
        except Exception as e:
            print("Push failed (SDK) - likely requires auth or registry setup:", e)
    except Exception as e:
        print("Tag/push failed (SDK):", e)
elif DOCKER_CLI:
    try:
        subprocess.run(["docker", "tag", image_tag, remote_tag], check=True)
        print("Tagged (CLI):", remote_tag)
        # Attempt push but it may fail without credentials
        subprocess.run(["docker", "push", remote_tag], check=True)
        print("Pushed (CLI):", remote_tag)
    except Exception as e:
        print("Tag/push failed (CLI) - likely requires auth or registry:", e)
# 👉 Why useful:
# Pushing images is key to delivering container artifacts to registries for deployment.
# ============================================================


# 10. Copy files into/from a container (docker cp)
# Practical use case: Extract logs or copy config files for inspection
src_host_file = Path("example.txt")
src_host_file.write_text("example content")
if DOCKER_CLI:
    try:
        # Copy host -> container (requires container running)
        # We'll create a short-lived container for demo if none exists
        demo_name = "devops_cp_demo"
        subprocess.run(["docker", "run", "--rm", "-d", "--name", demo_name, "nginx:latest"], check=True)
        subprocess.run(["docker", "cp", str(src_host_file), f"{demo_name}:/tmp/example.txt"], check=True)
        out = subprocess.check_output(["docker", "exec", demo_name, "ls", "/tmp"], text=True)
        print("Files in container /tmp (CLI):", out.strip())
        subprocess.run(["docker", "rm", "-f", demo_name], check=True)
    except Exception as e:
        print("docker cp demo failed:", e)
else:
    print("Skipping docker cp demo: docker CLI not available.")
# 👉 Why useful:
# Useful for collecting artifacts, logs, or temporary configs from running containers.
# ============================================================


# 11. Inspect container/image metadata
# Practical use case: Read labels, config, and ports programmatically
if docker_client:
    try:
        imgs = docker_client.images.list()
        if imgs:
            meta = imgs[0].attrs
            print("Image metadata keys (SDK):", list(meta.keys())[:10])
    except Exception as e:
        print("Inspect failed (SDK):", e)
elif DOCKER_CLI:
    try:
        out = subprocess.check_output(["docker", "inspect", image_tag], text=True)
        inspected = json.loads(out)
        print("Image inspect (CLI) keys:", list(inspected[0].keys())[:10])
    except Exception as e:
        print("Inspect failed (CLI):", e)
# 👉 Why useful:
# Inspect allows automation to make decisions based on image labels, exposed ports, etc.
# ============================================================


# 12. Monitor container stats (CPU/memory)
# Practical use case: Quick resource check for an actively running container
if docker_client:
    try:
        # Use non-streaming stats for a one-shot sample
        demo = None
        try:
            demo = docker_client.containers.run("nginx:latest", detach=True, name="devops_stats_demo")
            stats = demo.stats(stream=False)
            # stats is a dict-like JSON; print a few keys
            print("Container stats (SDK) keys sample:", list(stats.keys())[:5])
        finally:
            if demo:
                demo.remove(force=True)
    except Exception as e:
        print("Stats failed (SDK):", e)
elif DOCKER_CLI:
    print("Docker CLI stats (streaming) requires interactive handling; skipping sample.")
# 👉 Why useful:
# Resource metrics help detect overloaded containers and tune limits.
# ============================================================


# 13. Prune unused images to free disk space
# Practical use case: Cleanup build agents before new pipeline runs
if DOCKER_CLI:
    try:
        subprocess.run(["docker", "image", "prune", "-f"], check=True)
        print("Pruned unused images (CLI)")
    except Exception as e:
        print("Prune failed (CLI):", e)
else:
    print("Skipping prune: docker CLI not available.")
# 👉 Why useful:
# Prevent disk exhaustion on CI/CD runners by cleaning stale images/artifacts.
# ============================================================


# 14. Create and use a custom network
# Practical use case: Network-isolate integration test environment
net_name = "devops_test_net"
if docker_client:
    try:
        try:
            net = docker_client.networks.get(net_name)
        except Exception:
            net = docker_client.networks.create(net_name, driver="bridge")
        # create a short-lived container attached to this network
        c = docker_client.containers.run("nginx:latest", detach=True, network=net_name, name="devops_net_demo")
        print("Started container on network (SDK):", net_name)
        c.remove(force=True)
        net.remove()
    except Exception as e:
        print("Network demo failed (SDK):", e)
elif DOCKER_CLI:
    try:
        subprocess.run(["docker", "network", "create", net_name], check=True)
        subprocess.run(["docker", "run", "--rm", "--network", net_name, "nginx:latest", "true"], check=True)
        subprocess.run(["docker", "network", "rm", net_name], check=True)
        print("Network demo (CLI) completed")
    except Exception as e:
        print("Network demo failed (CLI):", e)
# 👉 Why useful:
# Use custom networks to simulate multi-service environments during tests.
# ============================================================


# 15. Save and load image to/from tar archive
# Practical use case: Transfer image artifact between air-gapped environments
archive_path = "example_image.tar"
if DOCKER_CLI:
    try:
        subprocess.run(["docker", "save", "-o", archive_path, image_tag], check=True)
        print("Saved image to", archive_path)
        # Load back (demo)
        subprocess.run(["docker", "load", "-i", archive_path], check=True)
        print("Loaded image from", archive_path)
    except Exception as e:
        print("Save/load failed (CLI):", e)
else:
    print("Skipping save/load: docker CLI not available.")
# 👉 Why useful:
# TAR archives of images are used to move containers to disconnected environments or for offline caching.
# ============================================================
