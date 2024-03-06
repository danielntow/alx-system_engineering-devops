#!/usr/bin/python3
"""
2-recurse
"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of hot articles.
        after (str): Token to paginate through results.

    Returns:
        list or None: A list containing the titles of hot articles, or None if
        no results are found for the subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {"User-Agent": "my_custom_user_agent"}

    # Parameters for pagination
    params = {"after": after, "limit": 100}

    # Make a request to the Reddit API
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()

        # Extract titles of hot articles and add them to the list
        posts = data["data"]["children"]
        for post in posts:
            hot_list.append(post["data"]["title"])

        # Check if there are more results to paginate through
        after = data["data"]["after"]
        if after:
            # Recursive call with the updated 'after' parameter
            recurse(subreddit, hot_list, after)
        else:
            # Return the final list of titles
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
        subreddit = sys.argv[1]
        result = recurse(subreddit)
        if result is not None:
            print(len(result))
        else:
            print("None")
