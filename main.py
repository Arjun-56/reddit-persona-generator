from reddit_scraper import fetch_user_data, get_username_from_url

if __name__ == "__main__":
    url = input("Enter Reddit profile URL: ")
    username = get_username_from_url(url)

    print(f"\nScraping data for user: {username}...")
    posts, comments = fetch_user_data(username)

    print("\n--- POSTS SAMPLE ---")
    if posts:
        for i, post in enumerate(posts[:10], 1):
            print(f"\nPost {i}:\n{post}")
    else:
        print("No posts found.")

    print("\n--- COMMENTS SAMPLE ---")
    if comments:
        for i, comment in enumerate(comments[:10], 1):
            print(f"\nComment {i}:\n{comment}")
    else:
        print("No comments found.")
