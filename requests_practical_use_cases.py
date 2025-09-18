# ============================================================
# Practical DevOps examples with Python requests module
# ============================================================


import requests


# 1. requests.get()
# Practical use case: Health-check a service
try:
    resp = requests.get("https://httpbin.org/get")
    print("Health-check status:", resp.status_code)
except requests.RequestException as e:
    print("Service unreachable:", e)
# 👉 Why useful:
# Automate availability checks for services, APIs, or endpoints.
# ============================================================

# 2. requests.get() with query params
# Practical use case: Call API with parameters
resp = requests.get("https://httpbin.org/get", params={"env": "prod", "version": "1.0"})
print("API call with params:", resp.json())
# 👉 Why useful:
# Pass filters/queries to monitoring or cloud APIs.
# ============================================================

# 3. requests.post()
# Practical use case: Send data to webhook (e.g., Slack, Teams)
payload = {"text": "Deployment finished successfully 🚀"}
try:
    resp = requests.post("https://httpbin.org/post", json=payload)
    print("Webhook response:", resp.json())
except requests.RequestException as e:
    print("Webhook failed:", e)
# 👉 Why useful:
# Notify chat tools (Slack, Teams) about CI/CD pipeline status.
# ============================================================

# 4. requests.post() with auth
# Practical use case: Authenticate to API
resp = requests.post("https://httpbin.org/post", auth=("user", "pass"))
print("Authenticated request:", resp.json())
# 👉 Why useful:
# Many APIs require authentication for security.
# ============================================================

# 5. requests.put()
# Practical use case: Update resource in REST API
update = {"replicas": 5}
resp = requests.put("https://httpbin.org/put", json=update)
print("PUT response:", resp.json())
# 👉 Why useful:
# Manage infrastructure or service settings via APIs.
# ============================================================

# 6. requests.delete()
# Practical use case: Delete resource
resp = requests.delete("https://httpbin.org/delete")
print("DELETE response:", resp.json())
# 👉 Why useful:
# Automate cleanup of cloud resources via REST APIs.
# ============================================================

# 7. requests.head()
# Practical use case: Check if artifact exists without downloading
resp = requests.head("https://httpbin.org/image/png")
print("HEAD request headers:", resp.headers.get("Content-Type"))
# 👉 Why useful:
# Validate files/artifacts before fetching them.
# ============================================================

# 8. Timeout handling
# Practical use case: Fail fast if API is slow
try:
    resp = requests.get("https://httpbin.org/delay/3", timeout=2)
except requests.Timeout:
    print("Request timed out")
# 👉 Why useful:
# Avoid blocking automation scripts on unresponsive APIs.
# ============================================================

# 9. Streaming large responses
# Practical use case: Download large logs/artifacts
resp = requests.get("https://httpbin.org/stream/3", stream=True)
for line in resp.iter_lines():
    if line:
        print("Streamed line:", line.decode())
# 👉 Why useful:
# Efficiently process logs or metrics without loading them fully into memory.
# ============================================================

# 10. Custom headers
# Practical use case: Send API token
headers = {"Authorization": "Bearer my-token"}
resp = requests.get("https://httpbin.org/headers", headers=headers)
print("Headers response:", resp.json())
# 👉 Why useful:
# Pass secrets/tokens to secured APIs.
# ============================================================

# 11. Session object
# Practical use case: Reuse connection for multiple requests
with requests.Session() as session:
    session.headers.update({"Authorization": "Bearer session-token"})
    r1 = session.get("https://httpbin.org/get")
    r2 = session.get("https://httpbin.org/anything")
    print("Session request 1:", r1.status_code)
    print("Session request 2:", r2.status_code)
# 👉 Why useful:
# Speeds up multiple API calls (reuses TCP connection).
# ============================================================

# 12. SSL verification
# Practical use case: Skip SSL verification in dev (not recommended for prod!)
try:
    resp = requests.get("https://self-signed.badssl.com/", verify=False)
    print("SSL skipped status:", resp.status_code)
except requests.RequestException:
    print("Could not connect")
# 👉 Why useful:
# Sometimes needed for dev/test environments with self-signed certs.
# ============================================================

# 13. File upload
# Practical use case: Upload artifact to server
files = {"file": ("example.txt", b"sample data")}
resp = requests.post("https://httpbin.org/post", files=files)
print("File upload response:", resp.json())
# 👉 Why useful:
# Upload logs, configs, or artifacts to monitoring/storage APIs.
# ============================================================

# 14. JSON response parsing
# Practical use case: Extract data from API
resp = requests.get("https://httpbin.org/json")
data = resp.json()
print("Extracted slideshow title:", data.get("slideshow", {}).get("title"))
# 👉 Why useful:
# Easily parse API responses for monitoring or CI/CD.
# ============================================================

# 15. Error handling
# Practical use case: Fail gracefully
try:
    resp = requests.get("https://httpbin.org/status/500")
    resp.raise_for_status()
except requests.HTTPError as e:
    print("Request failed with HTTP error:", e)
# 👉 Why useful:
# Proper error handling avoids silent pipeline failures.
# ============================================================
