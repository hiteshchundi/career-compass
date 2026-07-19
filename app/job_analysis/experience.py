from .regex import EXPERIENCE_REGEX


def extract_experience(text: str) -> str | None:
    match = EXPERIENCE_REGEX.search(text)

    if not match:
        return None

    return match.group()