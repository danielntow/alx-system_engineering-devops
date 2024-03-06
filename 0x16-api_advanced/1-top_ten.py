#!/usr/bin/python3
"""
1-top_ten
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of
    the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {"User-Agent": "my_custom_user_agent"}

    # Make a request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()

        # Extract and print the titles of the first 10 hot posts
        posts = data["data"]["children"][:10]
        for post in posts:
            print(post["data"]["title"])

    elif response.status_code == 302:
        # Redirect indicates an invalid subreddit
        print(None)

    else:
        # Print error message
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    # Test the function with command-line arguments
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
