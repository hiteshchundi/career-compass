import re

from .recommendations import generate_recommendations
from .types import MatchResult


DEGREE_RANK = {"associate": 1, "bachelor": 2, "master": 3, "doctorate": 4}


def years_of_experience(value) -> float:
    if isinstance(value, (int, float)):
        return max(0.0, float(value))
    if isinstance(value, list):
        return max((years_of_experience(item) for item in value), default=0.0)
    if isinstance(value, dict):
        return years_of_experience(value.get("duration"))
    match = re.search(r"\b(\d{1,2}(?:\.\d+)?)\s*\+?\s*years?\b", str(value or ""), re.I)
    return float(match.group(1)) if match else 0.0


def degree_rank(value) -> int:
    if isinstance(value, list):
        return max((degree_rank(item) for item in value), default=0)
    if isinstance(value, dict):
        return degree_rank(value.get("degree"))
    return DEGREE_RANK.get(str(value or "").lower(), 0)


class MatchingEngine:
    def compare(self, resume: dict, job: dict) -> MatchResult:
        if hasattr(resume, "model_dump"):
            resume = resume.model_dump()
        if hasattr(job, "model_dump"):
            job = job.model_dump()

        resume_skills = set(resume.get("skills") or [])
        required_skills = set(job.get("required_skills") or [])
        matched = sorted(resume_skills & required_skills)
        missing = sorted(required_skills - resume_skills)

        required_years = years_of_experience(job.get("experience"))
        resume_years = years_of_experience(resume.get("experience"))
        required_degree = degree_rank(job.get("education"))
        resume_degree = degree_rank(resume.get("education"))
        experience_match = resume_years >= required_years if required_years else None
        education_match = resume_degree >= required_degree if required_degree else None
        alternative = bool(job.get("education_or_experience") and required_years and required_degree)

        weights = []
        if required_skills:
            weights.append((70, len(matched) / len(required_skills)))
        if alternative:
            weights.append((20, max(min(resume_years / required_years, 1), float(bool(education_match)))))
        else:
            if required_years:
                weights.append((20, min(resume_years / required_years, 1)))
            if required_degree:
                weights.append((10, float(bool(education_match))))
        score = round(100 * sum(weight * ratio for weight, ratio in weights) /
                      sum(weight for weight, _ in weights), 2) if weights else 0.0

        return MatchResult(
            match_score=score,
            matched_skills=matched,
            missing_skills=missing,
            extra_skills=sorted(resume_skills - required_skills),
            experience_match=experience_match,
            education_match=education_match,
            education_or_experience=alternative,
            recommendations=generate_recommendations(
                missing_skills=missing,
                experience_match=experience_match if not alternative or not education_match else None,
                education_match=education_match if not alternative or not experience_match else None,
            ) if weights else ["The job description has no recognizable requirements to assess."],
        )
