import os
from dotenv import load_dotenv
import praw

# Load environment variables
load_dotenv()

def get_username_from_url(url: str) -> str:
    return url.rstrip("/").split("/")[-1]

def fetch_user_data(username: str, limit: int = 20):
    print("User agent is:", os.getenv("REDDIT_USER_AGENT"))
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT", "persona-generator-script")
    )

    try:
        redditor = reddit.redditor(username)
        posts = []
        comments = []

        for sub in redditor.submissions.new(limit=limit):
            text = (sub.title + "\n" + sub.selftext).strip()
            if text:
                posts.append(text)

        for com in redditor.comments.new(limit=limit):
            if com.body:
                comments.append(com.body)

        return posts, comments

    except Exception as exc:
        print(f"[!] Error fetching data for {username}: {exc}")
        return [], []

