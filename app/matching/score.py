import re


def _years(value) -> int:
    """
    Convert experience values into an integer number of years.

    Accepts:
    - 3
    - 3.0
    - "3+ years"
    - "Minimum 5 years"
    - ["Worked 3 years at TCS", "2 years at Amazon"]
    """

    if value is None:
        return 0

    if isinstance(value, (int, float)):
        return int(value)

    if isinstance(value, list):
        value = " ".join(str(v) for v in value)

    match = re.search(r"\d+", str(value))

    return int(match.group()) if match else 0


def calculate_match_score(
    *,
    resume_skills,
    required_skills,
    resume_experience,
    required_experience,
    resume_education,
    required_education,
):
    """
    Weighted score:

    Skills      : 70%
    Experience  : 20%
    Education   : 10%
    """

    # ---------- Skills ----------
    resume_skills = set(resume_skills or [])
    required_skills = set(required_skills or [])

    if required_skills:
        skill_score = (
            len(resume_skills & required_skills)
            / len(required_skills)
        )
    else:
        skill_score = 1.0

    # ---------- Experience ----------
    resume_years = _years(resume_experience)
    required_years = _years(required_experience)

    if required_years == 0:
        experience_score = 1.0
    else:
        experience_score = min(
            resume_years / required_years,
            1.0,
        )

    # ---------- Education ----------
    resume_education = set(resume_education or [])
    required_education = set(required_education or [])

    if not required_education:
        education_score = 1.0
    else:
        education_score = float(
            bool(
                resume_education & required_education
            )
        )

    total = (
        skill_score * 70
        + experience_score * 20
        + education_score * 10
    )

    return round(total, 2)