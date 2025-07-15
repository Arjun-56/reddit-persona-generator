import requests
from bs4 import BeautifulSoup
import time
import re

def get_username_from_url(url):
    return url.strip("/").split("/")[-1]

def fetch_user_data(username):
    base_url = f"https://www.reddit.com/user/{username}/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    posts_url = base_url + "submitted/"
    comments_url = base_url + "comments/"

    print(f"Scraping posts from: {posts_url}")
    posts = scrape_reddit_page(posts_url, headers)

    print(f"Scraping comments from: {comments_url}")
    comments = scrape_reddit_page(comments_url, headers)

    return posts, comments

def scrape_reddit_page(url, headers, limit=20):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Failed to access {url}. Status: {response.status_code}")
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        results = []

        for tag in soup.find_all(["p", "h1", "h2", "h3", "span", "div"]):
            text = tag.get_text(strip=True)
            if text and 20 < len(text) < 1000:  # avoid very short/long junk
                results.append(text)
                if len(results) >= limit:
                    break

        return results

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return []

if __name__ == "__main__":
    url = input("Enter Reddit profile URL (e.g. https://www.reddit.com/user/kojied/): ")
    username = get_username_from_url(url)
    posts, comments = fetch_user_data(username)

    print(f"\nFound {len(posts)} posts and {len(comments)} comments.")
    print("Sample post:", posts[0] if posts else "None")
    print("Sample comment:", comments[0] if comments else "None")
