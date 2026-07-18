from pathlib import Path

from docx import Document


class DOCXExtractionError(Exception):
    """Raised when text extraction from a DOCX file fails."""


def extract_text(file_path: str | Path) -> str:
    """
    Extract text from a DOCX document.

    Args:
        file_path: Path to the DOCX file.

    Returns:
        The extracted text as a single string.

    Raises:
        FileNotFoundError:
            If the file does not exist.

        DOCXExtractionError:
            If the document cannot be read or contains no extractable text.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    try:
        document = Document(path)

        paragraphs = [
            paragraph.text.strip()
            for paragraph in document.paragraphs
            if paragraph.text.strip()
        ]

        extracted_text = "\n".join(paragraphs).strip()

        if not extracted_text:
            raise DOCXExtractionError(
                "No text could be extracted from the DOCX document."
            )

        return extracted_text

    except DOCXExtractionError:
        raise

    except Exception as exc:
        raise DOCXExtractionError(
            f"Failed to extract DOCX text: {exc}"
        ) from exc