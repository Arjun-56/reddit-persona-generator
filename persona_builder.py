import openai
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv()  # Loads API key from .env file
print("Loaded key:", os.getenv("OPENAI_API_KEY")[:10], "...")

openai.api_key = os.getenv("OPENAI_API_KEY")


def build_persona(posts, comments, username):
    content = "\n\n".join(posts + comments)

    prompt = f"""
You are an AI that analyzes Reddit users based on their posts and comments.

Based on the following content from the Reddit user **{username}**, generate a persona describing their:

- Interests
- Personality traits
- Opinions/beliefs
- Writing style
- Any inferred demographics (age group, gender, location — if detectable)

Also, for each point, cite the exact phrase or post/comment you used as evidence.

Here is the content:

\"\"\"
{content}
\"\"\"

Format your answer as a readable profile.
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response['choices'][0]['message']['content']
