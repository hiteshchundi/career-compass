def calculate_match_score(
    *,
    resume_skills: set[str],
    required_skills: set[str],
    resume_experience: int | None,
    required_experience: int | None,
    resume_education: list[str],
    required_education: list[str],
) -> float:
    """
    Weighted score:

    Skills      : 70%
    Experience  : 20%
    Education   : 10%
    """

    # ---------- Skills ----------
    if required_skills:
        skill_score = (
            len(resume_skills & required_skills)
            / len(required_skills)
        )
    else:
        skill_score = 1.0

    # ---------- Experience ----------
    if required_experience is None:
        experience_score = 1.0
    elif resume_experience is None:
        experience_score = 0.0
    else:
        experience_score = min(
            resume_experience / required_experience,
            1.0,
        )

    # ---------- Education ----------
    if not required_education:
        education_score = 1.0
    else:
        education_score = float(
            bool(
                set(resume_education)
                & set(required_education)
            )
        )

    total = (
        skill_score * 70
        + experience_score * 20
        + education_score * 10
    )

    return round(total, 2)