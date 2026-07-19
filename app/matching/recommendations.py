def generate_recommendations(
    *,
    missing_skills: list[str],
    experience_match: bool,
    education_match: bool,
) -> list[str]:

    recommendations = []

    for skill in missing_skills:
        recommendations.append(
            f"Add evidence of '{skill}' through projects or work experience."
        )

    if not experience_match:
        recommendations.append(
            "Highlight projects that demonstrate equivalent experience."
        )

    if not education_match:
        recommendations.append(
            "Verify that your education section clearly matches the job requirements."
        )

    return recommendations