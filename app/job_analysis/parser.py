import re

from .skills import find_skills
from .experience import extract_experience
from .education import extract_education
from .keywords import extract_keywords
from .regex import TITLE_REGEX


class JobParser:

    def parse(self, text: str) -> dict:

        required = set()
        preferred = set()
        preference = False
        for line in text.splitlines():
            lowered = line.lower().strip()
            if any(marker in lowered for marker in ("preferred qualifications", "nice to have", "bonus skills", "preferred skills")):
                preference = True
            elif any(marker in lowered for marker in ("required qualifications", "minimum qualifications", "requirements", "must have")):
                preference = False
            skills = find_skills(line)
            (preferred if preference or "preferred" in lowered or "nice to have" in lowered else required).update(skills)

        title = None

        title_match = TITLE_REGEX.search(text)

        if title_match:
            title = title_match.group()

        education = extract_education(text)
        experience = extract_experience(text)
        alternative = bool(education and experience and any(
            re.search(r"(?:degree|bachelor|master).{0,100}\bor\b.{0,100}(?:\d+\s*\+?\s*years?|equivalent experience)", line, re.I)
            or re.search(r"\d+\s*\+?\s*years?.{0,100}\bor\b.{0,100}(?:degree|bachelor|master)", line, re.I)
            for line in text.splitlines()
        ))

        return {
            "title": title,
            "required_skills": sorted(required),
            "preferred_skills": sorted(preferred - required),
            "experience": experience,
            "education": education,
            "education_or_experience": alternative,
            "keywords": extract_keywords(text),
            "raw_text": text,
        }
