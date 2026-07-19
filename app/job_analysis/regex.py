import re

EXPERIENCE_REGEX = re.compile(
    r"(\d+)\+?\s*(?:-|to)?\s*\d*\+?\s*years?",
    re.IGNORECASE,
)

TITLE_REGEX = re.compile(
    r"(data engineer|data analyst|software engineer|backend engineer|ml engineer|ai engineer|python developer)",
    re.IGNORECASE,
)

EDUCATION_REGEX = re.compile(
    r"(bachelor|master|b\.?tech|m\.?tech|b\.?e|m\.?e|degree)",
    re.IGNORECASE,
)