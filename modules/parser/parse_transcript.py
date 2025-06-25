import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env

openai.api_key = os.getenv("OPENAI_API_KEY")

def parse_recipe_from_text(transcript_text):
    prompt = f"""
Given the following cooking transcript, extract a structured recipe JSON including:
- ingredients (list)
- steps (each with step text, action, ingredients involved, duration in seconds if mentioned)

Transcript:
\"\"\"
{transcript_text}
\"\"\"

Return JSON only.
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response['choices'][0]['message']['content']
