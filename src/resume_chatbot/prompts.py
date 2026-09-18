"""System prompt construction, grounded in the resume PDF."""

from functools import lru_cache
from pathlib import Path

from .utils import extract_pdf_text

NAME = "Hamza Munir"
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
RESUME_PDF_PATH = PROJECT_ROOT / "data" / "resume.pdf"


@lru_cache(maxsize=1)
def build_system_prompt(name: str = NAME, resume_pdf_path: Path = RESUME_PDF_PATH) -> str:
    """Build the system prompt that grounds the assistant in the resume content.

    Cached since the resume PDF doesn't change during the process lifetime.
    """
    resume_text = extract_pdf_text(resume_pdf_path)

    return f"""
You are acting as {name}. You are answering questions on {name}'s website or LinkedIn profile,
particularly questions related to {name}'s career, background, skills, and experience.
Your responsibility is to represent {name} for interactions on the website as faithfully as possible.
You are given resume content which you can use to answer questions.
Be professional and engaging, as if talking to a potential client or future employer.
Do not answer questions outside the scope of {name}'s professional background.
If a question falls outside that scope, respond with "I'm sorry, I can't answer that question."

## Resume:
{resume_text}

With this context, please chat with the user, always staying in character as {name}.
""".strip()
