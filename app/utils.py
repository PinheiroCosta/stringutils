import tomllib


def get_version() -> str:
    with open("pyproject.toml", "rb") as f:
        data = tomllib.load(f)
    version = data.get("tool", {}).get("poetry", {}).get("version")
    if not isinstance(version, str):
        raise TypeError("Invalid or missing version in pyproject.toml")
    return version
