import base64
import requests
from nacl import public, encoding

def get_repo_public_key(token: str, repo: str) -> dict:
    r = requests.get(
        f"https://api.github.com/repos/{repo}/actions/secrets/public-key",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
        },
    )
    r.raise_for_status()
    return r.json()

def encrypt_secret(public_key_b64: str, secret: str) -> str:
    pk = public.PublicKey(
        base64.b64decode(public_key_b64),
        encoding.RawEncoder,
    )
    sealed_box = public.SealedBox(pk)
    encrypted = sealed_box.encrypt(secret.encode("utf-8"))
    return base64.b64encode(encrypted).decode("utf-8")

def put_repo_secret(token: str, repo: str, name: str, value: str):
    key = get_repo_public_key(token, repo)
    encrypted_value = encrypt_secret(key["key"], value)

    r = requests.put(
        f"https://api.github.com/repos/{repo}/actions/secrets/{name}",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
        },
        json={
            "encrypted_value": encrypted_value,
            "key_id": key["key_id"],
        },
    )
    r.raise_for_status()