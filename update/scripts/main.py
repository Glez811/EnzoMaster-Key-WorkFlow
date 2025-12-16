import os

if os.environ.get("GITHUB_APP_ID"):
    print("GitHub App already exists — skipping creation")
    exit(0)