import tomllib


def get_version() -> str:
    with open("pyproject.toml", "rb") as f:
        data = tomllib.load(f)
    return data["tool"]["poetry"]["version"]
