from reddit_scraper import fetch_user_data, get_username_from_url

if __name__ == "__main__":
    url = input("Enter Reddit profile URL: ")
    username = get_username_from_url(url)

    print(f"\n🔍 Scraping data for user: {username}...")
    posts, comments = fetch_user_data(username)

    print("\n📄 --- POSTS SAMPLE ---")
    for i, post in enumerate(posts, 1):
        print(f"\nPost {i}:\n{post}")

    print("\n💬 --- COMMENTS SAMPLE ---")
    for i, comment in enumerate(comments, 1):
        print(f"\nComment {i}:\n{comment}")
