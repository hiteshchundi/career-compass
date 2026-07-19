from .skills import SKILL_CATALOG
from .experience import extract_experience
from .education import extract_education
from .keywords import extract_keywords
from .regex import TITLE_REGEX


class JobParser:

    def parse(self, text: str) -> dict:

        text_lower = text.lower()

        skills = []

        for canonical, aliases in SKILL_CATALOG.items():

            if any(alias in text_lower for alias in aliases):
                skills.append(canonical)

        title = None

        title_match = TITLE_REGEX.search(text)

        if title_match:
            title = title_match.group()

        return {
            "title": title,
            "required_skills": sorted(skills),
            "preferred_skills": [],
            "experience": extract_experience(text),
            "education": extract_education(text),
            "keywords": extract_keywords(text),
            "raw_text": text,
        }