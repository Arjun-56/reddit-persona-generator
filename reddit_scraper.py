import os
import praw
from dotenv import load_dotenv

load_dotenv()

def get_username_from_url(url):
    return url.strip("/").split("/")[-1]

def fetch_user_data(username, limit=20):
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT"),
    )

    user = reddit.redditor(username)

    posts = []
    comments = []

    try:
        for post in user.submissions.new(limit=limit):
            content = f"{post.title}\n{post.selftext}".strip()
            if content:
                posts.append(content)

        for comment in user.comments.new(limit=limit):
            if comment.body:
                comments.append(comment.body)

    except Exception as e:
        print(f"Error fetching data: {e}")

    return posts, comments

if __name__ == "__main__":
    url = input("Enter Reddit profile URL: ")
    username = get_username_from_url(url)
    posts, comments = fetch_user_data(username)

    print(f"\nFound {len(posts)} posts and {len(comments)} comments.")
    print("Sample post:", posts[0] if posts else "None")
    print("Sample comment:", comments[0] if comments else "None")

