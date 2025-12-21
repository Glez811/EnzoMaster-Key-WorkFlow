import os

if os.environ.get("GITHUB_APP_ID"):
    print("GitHub App already exists — skipping creation")
    exit(0)

scripts.main
def build_manifest():
    return {
        "name": "EnzoMaster GitHub App",
        "url": "https://example.com"
    }


def manifest_url(manifest: dict) -> str:
    return manifest.get("url")

if __name__ != "__main__":
    raise RuntimeError("This module must be run as __main__")

# Required to mark scripts as a package
