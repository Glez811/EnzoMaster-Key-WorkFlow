from pathlib import Path

def write_env(path: Path, data: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for k, v in data.items():
            v = v.replace("\n", "\\n")
            f.write(f'{k}="{v}"\n')