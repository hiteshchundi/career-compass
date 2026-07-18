from pathlib import Path

from pypdf import PdfReader


class PDFExtractionError(Exception):
    """Raised when text extraction from a PDF fails."""


def extract_text(file_path: str | Path) -> str:
    """
    Extract text from a PDF document.

    Args:
        file_path: Path to the PDF file.

    Returns:
        The extracted text as a single string.

    Raises:
        FileNotFoundError:
            If the file does not exist.

        PDFExtractionError:
            If the PDF cannot be read or contains no extractable text.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    try:
        reader = PdfReader(path)

        pages = []

        for page in reader.pages:
            text = page.extract_text()

            if text:
                pages.append(text.strip())

        extracted_text = "\n\n".join(pages).strip()

        if not extracted_text:
            raise PDFExtractionError(
                "No text could be extracted from the PDF."
            )

        return extracted_text

    except PDFExtractionError:
        raise

    except Exception as exc:
        raise PDFExtractionError(
            f"Failed to extract PDF text: {exc}"
        ) from exc