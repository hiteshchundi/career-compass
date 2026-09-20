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

        return {
            "title": title,
            "required_skills": sorted(required),
            "preferred_skills": sorted(preferred - required),
            "experience": extract_experience(text),
            "education": extract_education(text),
            "keywords": extract_keywords(text),
            "raw_text": text,
        }
