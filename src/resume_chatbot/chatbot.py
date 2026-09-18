"""Streaming chat completion backed by the OpenAI API."""

import os
from collections.abc import Iterator

from dotenv import load_dotenv
from openai import OpenAI

from .prompts import build_system_prompt

load_dotenv(override=True)

MODEL = "gpt-4o-mini"

_client: OpenAI | None = None


def get_client() -> OpenAI:
    """Return a lazily-initialized, module-level OpenAI client."""
    global _client
    if _client is None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not set. Add it to your .env file.")
        _client = OpenAI(api_key=api_key)
    return _client


def chat(message: str, history: list[dict[str, str]]) -> Iterator[str]:
    """Stream a chat completion for the Gradio ChatInterface.

    Args:
        message: The latest user message.
        history: Prior turns, as OpenAI-style role/content dicts.

    Yields:
        The progressively-growing assistant reply, for streaming display.
    """
    messages = [
        {"role": "system", "content": build_system_prompt()},
        *history,
        {"role": "user", "content": message},
    ]

    response = get_client().chat.completions.create(
        model=MODEL,
        messages=messages,
        stream=True,
    )

    full_reply = ""
    for chunk in response:
        delta = chunk.choices[0].delta.content or ""
        full_reply += delta
        yield full_reply
