#!/usr/bin/python3
"""
Defines a function that returns a list of titles of
all hot posts of a subreddit
"""
import requests


def recurse(subreddit, after='', count=0, hot_list=[]):
    """
    Args:
        subreddit <str> : The subreddit to query
        after <str>     : Anchor point after which to get more posts
        count <int>     : Number of post items already seen
        hot_list <list> : The list of all hot post titles
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {"User-Agent": 'MyApp:v1.0'}
    params = {'after': after, 'count': count, 'limit': 100}

    resp = requests.get(url, headers=headers, params=params,
                        allow_redirects=False)

    if resp.status_code == 200:
        data = resp.json()
        after = data['data']['after']
        count += data['data']['dist']
        hot_posts = data['data']['children']

        for post in hot_posts:
            post_title = post['data']['title']
            hot_list.append(post_title)

        if after is not None:
            return recurse(subreddit, after, count)

        return hot_list
    else:
        return None
