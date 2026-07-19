from collections.abc import Callable

from app.ingestion.docx import extract_text as extract_docx_text
from app.ingestion.pdf import extract_text as extract_pdf_text
from app.ingestion.text import extract_text as extract_txt_text

Extractor = Callable[[str], str]

EXTRACTORS: dict[str, Extractor] = {
    "pdf": extract_pdf_text,
    "docx": extract_docx_text,
    "txt": extract_txt_text,
}