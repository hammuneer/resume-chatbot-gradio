# app/utils.py
from pypdf import PdfReader
from typing import Optional

def extract_linkedin_text(pdf_path: str) -> str:
    """
    Extracts text content from a PDF file.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Combined text of all pages in the PDF.
    """
    reader = PdfReader(pdf_path)
    linkedin_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            linkedin_text += text
    return linkedin_text