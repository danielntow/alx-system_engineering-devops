#!/usr/bin/python3
"""
100-count
"""
import requests

def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    Recursively queries the Reddit API, parses the titles of
    all hot articles, and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.
        after (str): The parameter used for pagination in Reddit API.
        count_dict (dict): Dictionary to store the count of each keyword.

    Returns:
        None
    """
    if count_dict is None:
        count_dict = {}

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

        # Extract the titles of hot articles
        posts = data["data"]["children"]
        for post in posts:
            # Convert to lowercase for case-insensitivity
            title = post["data"]["title"].lower()

            # Count occurrences of each keyword in the title
            for word in word_list:
                if word in count_dict:
                    count_dict[word] += title.count(word.lower())
                else:
                    count_dict[word] = title.count(word.lower())

        # Recursive call with the next 'after' parameter
        next_after = data["data"]["after"]
        if next_after:
            count_words(
                subreddit, word_list, after=next_after, count_dict=count_dict)
        else:
            # Print the sorted count
            sorted_count = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_count:
                print(f"{word}: {count}")

    elif response.status_code == 302:
        # Redirect indicates an invalid subreddit
        print("Invalid subreddit")

    else:
        # Print error message
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    # Test the function with command-line arguments
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
