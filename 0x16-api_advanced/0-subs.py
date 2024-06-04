#!/usr/bin/python3
"""Defines a function that returns total subscribers of a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """
    Args:
        subreddit <str>: The subreddit to query
    Return:
        Total subscribers of the given subreddit,
        0 if invalid subreddit or if an error occurs
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'MyApp:v1.0'}

    try:
        resp = requests.get(url, headers=headers, allow_redirects=False)
        # Check if the response status code is 200 (OK)
        if resp.status_code == 200:
            data = resp.json()
            # Safely extract the number of subscribers
            subscribers = data.get('data', {}).get('subscribers')
            return subscribers if subscribers is not None else 0
        else:
            return 0
    except requests.exceptions.RequestException:
        # Return 0 in case of any network-related issues
        return 0
