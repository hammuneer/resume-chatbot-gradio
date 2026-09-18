"""Gradio entry point for the resume chatbot."""

import gradio as gr

from .chatbot import chat
from .prompts import NAME

INTRO = f"""
# {NAME} — Resume Chatbot
Welcome! This chatbot represents **{NAME}** and can answer questions about his career,
background, skills, and experience based on his resume.
Please ask only professional or career-related questions.
"""


def build_demo() -> gr.Blocks:
    """Construct the Gradio Blocks app."""
    with gr.Blocks() as demo:
        gr.Markdown(INTRO)
        gr.ChatInterface(
            fn=chat,
            type="messages",
            textbox=gr.Textbox(placeholder=f"Ask a question about {NAME}'s professional background"),
        )
    return demo


def main() -> None:
    build_demo().launch()


if __name__ == "__main__":
    main()
