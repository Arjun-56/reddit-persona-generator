import os
from dotenv import load_dotenv
import openai

# Load .env and set API key
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is missing in .env")

openai.api_key = api_key  

def build_persona(posts, comments, username):
    content = "\n\n".join(posts + comments)

    prompt = f"""
You are an AI that analyzes a Reddit user.

Based on the following content from **{username}**, generate a persona covering:

- Interests
- Personality traits
- Opinions / beliefs
- Writing style
- Inferred demographics (age band, likely gender, location if detectable)

For each bullet, cite the exact phrase (post or comment) you used as evidence.

Content:
\"\"\" 
{content}
\"\"\" 

Return the profile as plain text.
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content
