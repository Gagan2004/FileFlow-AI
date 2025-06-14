# # groq_api.py
# import requests
# from config import GROQ_API_KEY, GROQ_MODEL

# def get_command_from_prompt(prompt: str) -> str:
#     headers = {
#         "Authorization": f"Bearer {GROQ_API_KEY}",
#         "Content-Type": "application/json"
#     }
#     data = {
#         "model": GROQ_MODEL,
#         "messages": [
#             {"role": "system", "content": "You are a helpful assistant that only outputs safe Linux shell commands based on user requests. No explanations, just the command."},
#             {"role": "user", "content": prompt}
#         ]
#     }

#     response = requests.post("https://api.groq.com/openai/v1/chat/completions", json=data, headers=headers)
#     response.raise_for_status()
#     return response.json()["choices"][0]["message"]["content"].strip()



# groq_api.py
import os
from groq import Groq
from workspace_context import get_workspace_context


# Initialize client using the Groq Python SDK
client = Groq(api_key="")

def get_command_from_prompt(prompt: str, model: str = "llama-3.3-70b-versatile") -> str:
    workspace_context = get_workspace_context()

    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": (
                "You are a helpful coding terminal assistant. "
                "The user is asking to perform file or directory operations. "
                "Here is their current workspace context:\n\n" + workspace_context+
                "DO NOT PRovide any explanation unless explicitly asked to , your primary AIM is to respnd in terms of COMMANDS"
            )},
            {"role": "user", "content": prompt}
        ],
        model=model
    )

    

    return response.choices[0].message.content.strip()
