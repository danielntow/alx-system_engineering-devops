#!/usr/bin/python3
"""
Recursive function to query the Reddit API and return a list
containing the titles of all hot articles for a given subreddit.
If no results are found, the function returns None.
"""
import requests


def get_hot_titles(subreddit, hot_titles=[], after=''):
    """
    Recursive function to get titles of hot articles for a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_titles (list): List to store the titles of hot articles.
        after (str): The parameter used for pagination in Reddit API.

    Returns:
        list: The list containing the titles of hot articles,
        or None if no results found.
    """
    user_agent = {'user-agent': 'fake_user_agent'}
    base_url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'

    response = requests.get(base_url, headers=user_agent)

    posts_data = response.json().get('data', {}).get("children", [])
    if not posts_data:
        return hot_titles

    for post in posts_data:
        hot_titles.append(post.get('data', {}).get('title'))

    next_after = response.json().get('data', {}).get('after', None)
    if next_after is not None:
        return get_hot_titles(subreddit, hot_titles, next_after)

    return hot_titles


if __name__ == "__main__":
    # Example usage
    subreddit_name = "programming"
    result = get_hot_titles(subreddit_name)
    if result is not None:
        print(result)
    else:
        print("No results found.")
