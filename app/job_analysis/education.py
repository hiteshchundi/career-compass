from .regex import EDUCATION_REGEX


def extract_education(text: str) -> list[str]:
    education = set()

    for match in EDUCATION_REGEX.finditer(text):
        education.add(match.group().lower())

    return sorted(education)