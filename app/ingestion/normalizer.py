import re


def normalize_text(text: str) -> str:
    """
    Normalize extracted document text.

    Operations:
    - Normalize line endings.
    - Remove trailing whitespace.
    - Collapse multiple blank lines.
    - Collapse consecutive spaces and tabs.
    - Trim leading and trailing whitespace.
    """

    # Normalize Windows and old Mac line endings
    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    # Remove trailing whitespace from each line
    lines = [line.rstrip() for line in text.split("\n")]

    text = "\n".join(lines)

    # Replace multiple spaces/tabs with a single space
    text = re.sub(r"[ \t]+", " ", text)

    # Replace 3 or more blank lines with just 2
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()