import requests

def exchange_manifest_code(code: str) -> dict:
    url = f"https://api.github.com/app-manifests/{code}/conversions"
    r = requests.post(
        url,
        headers={"Accept": "application/vnd.github+json"},
        timeout=10,
    )
    r.raise_for_status()
    return r.json()