from app.resume_analysis.extractors import extract_skills


def test_extract_skills():
    text = """
    Python
    FastAPI
    PostgreSQL
    Docker
    Git
    Pandas
    """

    skills = extract_skills(text)

    assert "python" in skills
    assert "fastapi" in skills
    assert "postgresql" in skills
    assert "docker" in skills
    assert "git" in skills
    assert "pandas" in skills