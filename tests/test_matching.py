from app.job_analysis.parser import JobParser
from app.matching.engine import MatchingEngine
from app.resume_analysis.parser import ResumeParser


def test_analysis_matches_canonical_skills_years_and_degree():
    resume = ResumeParser().parse("""
    Bachelor of Technology in Computer Science
    Software Engineer, 2020 - 2025
    Built PostgreSQL services with Python, FastAPI and Docker.
    """)
    job = JobParser().parse("""
    Required qualifications:
    3+ years of experience with Python, SQL, FastAPI and Docker.
    Bachelor's degree in Computer Science.
    Preferred qualifications:
    Kubernetes and AWS.
    """)
    result = MatchingEngine().compare(resume, job)

    assert job["required_skills"] == ["docker", "fastapi", "python", "sql"]
    assert job["preferred_skills"] == ["aws", "kubernetes"]
    assert result.matched_skills == job["required_skills"]
    assert result.missing_skills == []
    assert result.experience_match is True
    assert result.education_match is True
    assert result.match_score == 100


def test_missing_requirements_reduce_score_and_produce_recommendations():
    resume = ResumeParser().parse("Associate degree. 1 year of Python experience.")
    job = JobParser().parse("Requires Python, Docker, 3 years experience and a bachelor's degree.")
    result = MatchingEngine().compare(resume, job)

    assert result.matched_skills == ["python"]
    assert result.missing_skills == ["docker"]
    assert result.experience_match is False
    assert result.education_match is False
    assert 0 < result.match_score < 50
    assert len(result.recommendations) == 3


def test_unspecified_requirements_are_unknown_not_failed_or_perfect():
    result = MatchingEngine().compare(ResumeParser().parse("Hello"), JobParser().parse("Hello"))
    assert result.match_score == 0
    assert result.experience_match is None
    assert result.education_match is None
    assert "no recognizable requirements" in result.recommendations[0]


def test_skill_alias_requires_word_boundary():
    assert ResumeParser().parse("I work with gittery and sqlexpress.").skills == []
