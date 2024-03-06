#!/usr/bin/python3
"""
2-recurse
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): The list to store the titles of hot articles.
        after (str): The parameter used for pagination in Reddit API.

    Returns:
        list: The list containing the titles of hot articles, or
        None if no results found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {"User-Agent": "my_custom_user_agent"}

    # Include 'after' parameter if available
    params = {'after': after} if after else {}

    # Make a request to the Reddit API
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()

        # Extract the titles of hot articles and update the hot_list
        posts = data["data"]["children"]
        for post in posts:
            hot_list.append(post["data"]["title"])

        # Recursive call with the next 'after' parameter
        next_after = data["data"]["after"]
        if next_after:
            recurse(subreddit, hot_list, after=next_after)

        return hot_list

    elif response.status_code == 302:
        # Redirect indicates an invalid subreddit
        return None

    else:
        # Print error message and return None
        print(f"Error: {response.status_code}")
        return None


if __name__ == "__main__":
    # Test the function with command-line arguments
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
