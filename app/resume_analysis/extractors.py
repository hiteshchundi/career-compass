import re

from app.resume_analysis.skills import COMMON_SKILLS

from app.schemas.resume_analysis import (
    ContactInfo,
)


from app.resume_analysis.regex import (
    EMAIL_PATTERN,
    PHONE_PATTERN,
    LINKEDIN_PATTERN,
    GITHUB_PATTERN,
    first_match,
)

from app.schemas.resume_analysis import ContactInfo


def extract_contact(text: str) -> ContactInfo:
    email = first_match(EMAIL_PATTERN, text)
    phone = first_match(PHONE_PATTERN, text)
    linkedin = first_match(LINKEDIN_PATTERN, text)
    github = first_match(GITHUB_PATTERN, text)

    return ContactInfo(
        email=email,
        phone=phone,
        linkedin=linkedin,
        github=github,
    )


def extract_skills(text: str) -> list[str]:
    text = text.lower()

    found = []

    for skill in COMMON_SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):
            found.append(skill)

    return sorted(found)


def extract_education(text: str):
    return []


def extract_experience(text: str):
    return []


def extract_projects(text: str):
    return []


def extract_certifications(text: str):
    return []