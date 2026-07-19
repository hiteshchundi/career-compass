import re

from .recommendations import generate_recommendations
from .score import calculate_match_score
from .types import MatchResult

def extract_years(value):
    if value is None:
        return 0

    if isinstance(value, int):
        return value

    if isinstance(value, float):
        return int(value)

    if isinstance(value, list):
        text = " ".join(str(v) for v in value)
    else:
        text = str(value)

    match = re.search(r"\d+", text)

    if match:
        return int(match.group())

    return 0


class MatchingEngine:

    def compare(
        self,
        resume: dict,
        job: dict,
    ) -> MatchResult:
        
        if hasattr(resume, "model_dump"):
            resume = resume.model_dump()

        if hasattr(job, "model_dump"):
            job = job.model_dump()

        resume_skills = set(
            resume.get("skills", [])
        )

        required_skills = set(
    job.get("required_skills", [])
        )

        matched = sorted(
            resume_skills & required_skills
        )

        missing = sorted(
            required_skills - resume_skills
        )

        extra = sorted(
            resume_skills - required_skills
        )

        resume_experience = resume.get("experience")
        required_experience = job.get("experience")

        resume_years = extract_years(resume_experience)
        required_years = extract_years(required_experience)

        experience_match = resume_years >= required_years

        resume_education = resume.get(
            "education",
            [],
        )

        required_education = job.get(
            "education",
            [],
        )

        education_match = (
            bool(
                set(resume_education)
                & set(required_education)
            )
            or not required_education
        )

        score = calculate_match_score(
            resume_skills=resume_skills,
            required_skills=required_skills,
            resume_experience=resume_experience,
            required_experience=required_experience,
            resume_education=resume_education,
            required_education=required_education,
        )

        recommendations = generate_recommendations(
            missing_skills=missing,
            experience_match=experience_match,
            education_match=education_match,
        )

        return MatchResult(
            match_score=score,
            matched_skills=matched,
            missing_skills=missing,
            extra_skills=extra,
            experience_match=experience_match,
            education_match=education_match,
            recommendations=recommendations,
        )

    