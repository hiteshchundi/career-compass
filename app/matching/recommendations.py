def generate_recommendations(
    *,
    missing_skills: list[str],
    experience_match: bool | None,
    education_match: bool | None,
) -> list[str]:

    recommendations = []

    for skill in missing_skills:
        recommendations.append(
            f"If you have used '{skill}', show specific evidence in your work or projects."
        )

    if experience_match is False:
        recommendations.append(
            "Clarify your relevant dates and scope of work so your experience can be assessed."
        )

    if education_match is False:
        recommendations.append(
            "Verify that your education section clearly matches the job requirements."
        )

    return recommendations
