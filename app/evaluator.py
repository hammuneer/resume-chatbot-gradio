# # app/evaluator.py
# import json
# from openai import OpenAI
# from pydantic import ValidationError
# from .models import Evaluation
# from .prompts import evaluator_system_prompt
# import os
# from dotenv import load_dotenv

# load_dotenv(override=True)
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# openai = OpenAI(
#     api_key=OPENAI_API_KEY 
# )

# def evaluator_user_prompt(reply: str, message: str, history: list) -> str:
#     """
#     Create the prompt used to evaluate the assistant's reply.
#     """
#     return (
#         f"Here's the conversation between the User and the Agent: \n\n{history}\n\n"
#         f"Here's the latest message from the User: \n\n{message}\n\n"
#         f"Here's the latest response from the Agent: \n\n{reply}\n\n"
#         "Please evaluate the response."
#     )

# def evaluate(reply: str, message: str, history: list) -> Evaluation:
#     messages = [
#         {"role": "system", "content": evaluator_system_prompt},
#         {"role": "user", "content": evaluator_user_prompt(reply, message, history)}
#     ]
#     response = openai.chat.completions.create(model="gpt-4o-mini", messages=messages)
#     raw = response.choices[0].message.content
#     try:
#         parsed = json.loads(raw)
#         return Evaluation(**parsed)
#     except (json.JSONDecodeError, ValidationError) as e:
#         raise ValueError(f"Invalid response: {e}\nModel output:\n{raw}")
