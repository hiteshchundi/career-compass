from dataclasses import dataclass


@dataclass(slots=True)
class MatchResult:
    match_score: float

    matched_skills: list[str]

    missing_skills: list[str]

    extra_skills: list[str]

    experience_match: bool

    education_match: bool

    recommendations: list[str]