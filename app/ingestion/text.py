from pathlib import Path


def extract_text(path: str | Path) -> str:
    """
    Extract text from a plain text (.txt) file.
    """
    path = Path(path)

    return path.read_text(
        encoding="utf-8",
        errors="ignore",
    )