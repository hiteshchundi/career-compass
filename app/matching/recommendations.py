def generate_recommendations(
    *,
    missing_skills: list[str],
    experience_match: bool | None,
    education_match: bool | None,
) -> list[str]:

    recommendations = []

    for skill in missing_skills:
        recommendations.append(
            f"Add evidence of '{skill}' through projects or work experience."
        )

    if experience_match is False:
        recommendations.append(
            "Highlight projects that demonstrate equivalent experience."
        )

    if education_match is False:
        recommendations.append(
            "Verify that your education section clearly matches the job requirements."
        )

    return recommendations
