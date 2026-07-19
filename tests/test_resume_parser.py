from app.resume_analysis.parser import ResumeParser


def test_parser_returns_schema():
    parser = ResumeParser()

    result = parser.parse("Hello")

    assert result.contact is not None
    assert isinstance(result.skills, list)
    assert isinstance(result.education, list)
    assert isinstance(result.experience, list)
    assert isinstance(result.projects, list)
    assert isinstance(result.certifications, list)