import re
from datetime import date

from app.job_analysis.skills import find_skills
from app.resume_analysis.regex import (
    EMAIL_PATTERN,
    PHONE_PATTERN,
    LINKEDIN_PATTERN,
    GITHUB_PATTERN,
    first_match,
)

from app.schemas.resume_analysis import ContactInfo, Education, Experience


DEGREES = {
    "doctorate": r"\b(?:ph\.?d\.?|doctorate|doctoral)\b",
    "master": r"\b(?:master'?s?|m\.?tech\.?|m\.?e\.?|m\.?s\.?|mba)\b",
    "bachelor": r"\b(?:bachelor'?s?|b\.?tech\.?|b\.?e\.?|b\.?s\.?|bsc)\b",
    "associate": r"\bassociate'?s?\b",
}
YEARS_PATTERN = re.compile(r"\b(\d{1,2}(?:\.\d+)?)\s*\+?\s*years?\b", re.I)
DATE_RANGE = re.compile(
    r"\b(20\d{2}|19\d{2})\s*(?:-|–|—|to)\s*(20\d{2}|19\d{2}|present|current)\b", re.I
)


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
    return find_skills(text)


def extract_education(text: str) -> list[Education]:
    return [Education(institution="Not identified", degree=degree)
            for degree, pattern in DEGREES.items() if re.search(pattern, text, re.I)]


def extract_experience(text: str) -> list[Experience]:
    # Use the longest stated tenure or role; overlapping roles must not be added.
    candidates = [float(m.group(1)) for m in YEARS_PATTERN.finditer(text)
                  if float(m.group(1)) <= 60]
    for match in DATE_RANGE.finditer(text):
        start = int(match.group(1))
        end = date.today().year if match.group(2).lower() in {"present", "current"} else int(match.group(2))
        if start <= end <= date.today().year:
            candidates.append(float(end - start))
    if not candidates:
        return []
    return [Experience(company="Not identified", duration=f"{max(candidates):g} years")]


def extract_projects(text: str):
    return []


def extract_certifications(text: str):
    return []
