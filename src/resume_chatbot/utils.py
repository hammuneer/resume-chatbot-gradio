"""PDF text extraction helpers."""

from pathlib import Path

from pypdf import PdfReader


def extract_pdf_text(pdf_path: str | Path) -> str:
    """Extract and concatenate the text content of every page in a PDF.

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        The combined text of all pages.
    """
    reader = PdfReader(pdf_path)
    pages_text = (page.extract_text() or "" for page in reader.pages)
    return "".join(pages_text)
