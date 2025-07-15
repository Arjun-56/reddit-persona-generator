from reddit_scraper import fetch_user_data, get_username_from_url
from persona_builder import build_persona
import os

def save_persona(username, persona_text):
    os.makedirs("outputs", exist_ok=True)
    filepath = os.path.join("outputs", f"{username}.txt")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(persona_text)
    print(f"\n Persona saved to: {filepath}")

if __name__ == "__main__":
    url = input("Enter Reddit profile URL: ")
    username = get_username_from_url(url)

    print(f"\n Scraping data for user: {username}...")
    posts, comments = fetch_user_data(username)

    print("\n --- POSTS SAMPLE ---")
    for i, post in enumerate(posts[:5], 1):
        print(f"\nPost {i}:\n{post}")

    print("\n --- COMMENTS SAMPLE ---")
    for i, comment in enumerate(comments[:5], 1):
        print(f"\nComment {i}:\n{comment}")

    print(f"\n Generating persona using OpenAI for {username}...")
    persona = build_persona(posts, comments, username)

    save_persona(username, persona)
