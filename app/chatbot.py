# app/chatbot.py
from openai import OpenAI
from .prompts import system_prompt
# from .evaluator import evaluate
import os
from dotenv import load_dotenv


load_dotenv(override=True)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai = OpenAI(
    api_key=OPENAI_API_KEY 
)

# def rerun(reply: str, message: str, history: list, feedback: str) -> str:
#     updated_prompt = system_prompt + (
#         f"\n\n## Previous answer rejected\n"
#         f"You just tried to reply, but the quality control rejected it.\n"
#         f"## Attempted answer:\n{reply}\n"
#         f"## Reason for rejection:\n{feedback}\n"
#     )
#     messages = [
#         {"role": "system", "content": updated_prompt},
#         *history,
#         {"role": "user", "content": message}
#     ]
#     response = openai.chat.completions.create(model="gpt-4o-mini", messages=messages)
#     return response.choices[0].message.content

def chat(message: str, history: list):
    """
    Streamed chat function for Gradio.
    """
    
    system = system_prompt

    
     # Append user message manually to build the full message history
    messages = [{"role": "system", "content": system_prompt}] + history + [{"role": "user", "content": message}]


    # Stream reply from OpenAI
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        stream=True
    )

    full_reply = ""
    for chunk in response:
        delta = chunk.choices[0].delta.content or ""
        full_reply += delta
        yield full_reply  # Streaming part-by-part to Gradio

    # # After streaming is done, run evaluation
    # evaluation = evaluate(full_reply, message, history)
    # if not evaluation.is_acceptable:
    #     # Yield a retry message or re-stream rerun
    #     feedback = evaluation.feedback
    #     retry = rerun(full_reply, message, history, feedback)
    #     yield retry