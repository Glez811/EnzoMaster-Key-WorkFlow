import os
from pathlib import Path

from manifest import build_manifest, manifest_url
from playwright_flow import create_app_and_get_code
from github_api import exchange_manifest_code
from env_writer import write_env

def main():
    domain = os.environ["TRAEFIK_DOMAIN"]
    app_name = os.environ.get("APP_NAME", "My GitHub App")

    manifest = build_manifest(app_name, domain)
    url = manifest_url(manifest)

    code = create_app_and_get_code(url)
    app = exchange_manifest_code(code)

    env = {
        "GITHUB_APP_ID": str(app["id"]),
        "GITHUB_CLIENT_ID": app["client_id"],
        "GITHUB_CLIENT_SECRET": app["client_secret"],
        "GITHUB_APP_PRIVATE_KEY": app["pem"],
    }

    write_env(Path(".env.prod"), env)

    print("GitHub App created successfully")
    print(f"Install URL: https://github.com/apps/{app['slug']}/installations/new")

if __name__ == "__main__":
    main()