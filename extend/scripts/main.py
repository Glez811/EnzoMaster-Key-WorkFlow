from secrets import put_repo_secret

repo = os.environ.get("GITHUB_REPOSITORY")
token = os.environ.get("GITHUB_TOKEN")

if repo and token:
    for k, v in env.items():
        put_repo_secret(token, repo, k, v)