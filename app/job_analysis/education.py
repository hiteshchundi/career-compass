from app.resume_analysis.extractors import DEGREES
import re


def extract_education(text: str) -> list[str]:
    return [degree for degree, pattern in DEGREES.items()
            if re.search(pattern, text, re.I)]
