#!/usr/bin/python3
"""Defines a function that prints top 10 hot posts of a subreddit"""
import requests


def top_ten(subreddit):
    """
    Args:
        subreddit <str>: The subreddit to query
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {"User-Agent": 'MyApp:v1.0'}
    params = {'limit': 10}

    resp = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if resp.status_code == 200:
        data = resp.json()
        hot_posts = data['data']['children']
        for post in hot_posts:
            post_title = post['data']['title']
            print(post_title)
    else:
        print(None)
