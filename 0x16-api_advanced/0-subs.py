#!/usr/bin/python3
"""
0-subs
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the
    number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit,
        or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {"User-Agent": "my_custom_user_agent"}

    # Make a request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()

        # Extract and return the number of subscribers
        return data["data"]["subscribers"]

    elif response.status_code == 302:
        # Redirect indicates an invalid subreddit
        return 0

    else:
        # Print error message and return 0
        print(f"Error: {response.status_code}")
        return 0


if __name__ == "__main__":
    # Test the function with command-line arguments
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print("{:d}".format(subscribers))
