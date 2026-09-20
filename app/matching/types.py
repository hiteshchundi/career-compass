from dataclasses import dataclass


@dataclass(slots=True)
class MatchResult:
    match_score: float

    matched_skills: list[str]

    missing_skills: list[str]

    extra_skills: list[str]

    experience_match: bool | None

    education_match: bool | None

    recommendations: list[str]
