from .recommendations import generate_recommendations
from .score import calculate_match_score
from .types import MatchResult


class MatchingEngine:

    def compare(
        self,
        resume: dict,
        job: dict,
    ) -> MatchResult:

        resume_skills = set(
            resume.get("skills", [])
        )

        required_skills = set(
            job.get("skills", [])
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

        experience_match = (
            required_experience is None
            or (
                resume_experience is not None
                and resume_experience >= required_experience
            )
        )

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