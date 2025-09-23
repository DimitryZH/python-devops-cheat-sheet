# ============================================================
# Practical DevOps examples with Kubernetes (using kubernetes-client)
# ============================================================


import os
import sys
from pathlib import Path

try:
    from kubernetes import client, config, utils
    from kubernetes.stream import stream
except ImportError:
    print("⚠️  The 'kubernetes' Python package is not installed. Run 'pip install kubernetes' to enable examples.")
    client = None
    config = None
    utils = None

# ============================================================
# Practical examples
# ============================================================


if client and config:
    try:
        # 1. Load kubeconfig (default ~/.kube/config)
        # Practical use case: Authenticate to cluster
        config.load_kube_config()
        v1 = client.CoreV1Api()
        print("Connected to Kubernetes cluster via kubeconfig")
        # 👉 Why useful:
        # Needed in almost every automation script that interacts with the cluster.
        # ============================================================

        # 2. List namespaces
        # Practical use case: Inventory environments
        namespaces = [ns.metadata.name for ns in v1.list_namespace().items]
        print("Namespaces:", namespaces)
        # 👉 Why useful:
        # Helps DevOps scripts iterate through staging/prod/test environments.
        # ============================================================

        # 3. List pods in default namespace
        pods = [p.metadata.name for p in v1.list_namespaced_pod("default").items]
        print("Pods in default:", pods)
        # 👉 Why useful:
        # Checking pod health or presence is the first step in automation.
        # ============================================================

        # 4. Get logs of a pod
        if pods:
            logs = v1.read_namespaced_pod_log(name=pods[0], namespace="default", tail_lines=5)
            print(f"Logs from pod {pods[0]}:\n", logs)
        # 👉 Why useful:
        # Automating log retrieval for troubleshooting CI/CD.
        # ============================================================

        # 5. Execute a command in a pod
        if pods:
            exec_result = stream(
                v1.connect_get_namespaced_pod_exec,
                pods[0],
                "default",
                command=["echo", "Hello from inside pod"],
                stderr=True, stdin=False,
                stdout=True, tty=False,
            )
            print("Exec result:", exec_result)
        # 👉 Why useful:
        # Automating diag commands like 'ls', 'cat /etc/config', or health checks.
        # ============================================================

        # 6. Create a new namespace
        ns_body = client.V1Namespace(metadata=client.V1ObjectMeta(name="devops-demo"))
        try:
            v1.create_namespace(ns_body)
            print("Created namespace devops-demo")
        except Exception:
            print("Namespace already exists (devops-demo)")
        # 👉 Why useful:
        # Dynamically creating isolated environments for testing or previews.
        # ============================================================

        # 7. Deploy a simple pod (nginx)
        pod_manifest = {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {"name": "nginx-demo", "namespace": "devops-demo"},
            "spec": {"containers": [{"name": "nginx", "image": "nginx:1.25"}]},
        }
        try:
            v1.create_namespaced_pod(namespace="devops-demo", body=pod_manifest)
            print("Created pod nginx-demo in devops-demo")
        except Exception as e:
            print("Pod create failed (likely exists):", e)
        # 👉 Why useful:
        # Demonstrates programmatic workload deployment.
        # ============================================================

        # 8. Expose pod as a Service
        svc_manifest = client.V1Service(
            metadata=client.V1ObjectMeta(name="nginx-svc", namespace="devops-demo"),
            spec=client.V1ServiceSpec(
                selector={"app": "nginx"},
                ports=[client.V1ServicePort(protocol="TCP", port=80, target_port=80)],
            ),
        )
        try:
            v1.create_namespaced_service(namespace="devops-demo", body=svc_manifest)
            print("Created service nginx-svc")
        except Exception:
            print("Service already exists")
        # 👉 Why useful:
        # Automation often requires exposing pods/services programmatically.
        # ============================================================

        # 9. Scale a Deployment
        apps_v1 = client.AppsV1Api()
        dep = client.V1Deployment(
            metadata=client.V1ObjectMeta(name="nginx-dep", namespace="devops-demo"),
            spec=client.V1DeploymentSpec(
                replicas=1,
                selector={"matchLabels": {"app": "nginx"}},
                template=client.V1PodTemplateSpec(
                    metadata=client.V1ObjectMeta(labels={"app": "nginx"}),
                    spec=client.V1PodSpec(containers=[client.V1Container(name="nginx", image="nginx:1.25")]),
                ),
            ),
        )
        try:
            apps_v1.create_namespaced_deployment(namespace="devops-demo", body=dep)
            print("Created deployment nginx-dep")
        except Exception:
            print("Deployment already exists, scaling to 2 replicas...")
            dep_patch = {"spec": {"replicas": 2}}
            apps_v1.patch_namespaced_deployment("nginx-dep", "devops-demo", dep_patch)
        # 👉 Why useful:
        # Automating scaling up/down workloads is common in CI/CD and testing.
        # ============================================================

        # 10. Update labels on a pod
        if pods:
            body = {"metadata": {"labels": {"env": "test"}}}
            v1.patch_namespaced_pod(name=pods[0], namespace="default", body=body)
            print(f"Patched pod {pods[0]} with env=test label")
        # 👉 Why useful:
        # Dynamic labeling helps with environment tagging and selecting workloads.
        # ============================================================

        # 11. Create a ConfigMap
        cm = client.V1ConfigMap(
            metadata=client.V1ObjectMeta(name="demo-config", namespace="devops-demo"),
            data={"APP_MODE": "development", "TIMEOUT": "30"},
        )
        try:
            v1.create_namespaced_config_map("devops-demo", cm)
            print("Created ConfigMap demo-config")
        except Exception:
            print("ConfigMap already exists")
        # 👉 Why useful:
        # Storing application config for automation pipelines.
        # ============================================================

        # 12. Create a Secret
        secret = client.V1Secret(
            metadata=client.V1ObjectMeta(name="demo-secret", namespace="devops-demo"),
            string_data={"DB_PASSWORD": "supersecret"},
        )
        try:
            v1.create_namespaced_secret("devops-demo", secret)
            print("Created Secret demo-secret")
        except Exception:
            print("Secret already exists")
        # 👉 Why useful:
        # Automating sensitive credentials handling for deployments.
        # ============================================================

        # 13. List events
        events = v1.list_namespaced_event("default").items
        print("Recent events:", [f"{e.involved_object.kind}:{e.message}" for e in events[:3]])
        # 👉 Why useful:
        # Event inspection is key for troubleshooting automation failures.
        # ============================================================

        # 14. Delete pod
        try:
            v1.delete_namespaced_pod("nginx-demo", "devops-demo")
            print("Deleted pod nginx-demo")
        except Exception:
            print("Pod not found for deletion")
        # 👉 Why useful:
        # Automated cleanup of temporary workloads.
        # ============================================================

        # 15. Delete namespace
        try:
            v1.delete_namespace("devops-demo")
            print("Deleted namespace devops-demo")
        except Exception:
            print("Namespace not found for deletion")
        # 👉 Why useful:
        # Cleanup after tests avoids clutter and quota exhaustion.
        # ============================================================

    except Exception as e:
        print("❌ Could not run Kubernetes examples:", e)
else:
    print("Kubernetes SDK not available — skipping examples.")
# ============================================================