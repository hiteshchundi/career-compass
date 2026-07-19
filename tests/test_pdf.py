from pathlib import Path

from app.ingestion.pdf import extract_text

def test_extract_text():
    pdf_path = Path("tests/data/sample_resume.pdf")

    text = extract_text(pdf_path)

    assert text
    assert "John Doe" in text
    assert "Python" in text
    assert "SQL" in text
    assert "PostgreSQL" in text
    assert "FastAPI" in text
    assert "Docker" in text