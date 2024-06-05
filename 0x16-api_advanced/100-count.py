#!/usr/bin/python3
"""
Defines a function that parses the title of all hot articles,
and prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list):
    """
    Prints the sorted count of given keywords

    Args:
        subredit <str>   : The subreddit to query
        word_list <list> : A list containing the words to count
    """
    # Call recurse function to return the list of hot titles
    hot_list = recurse(subreddit)
    if hot_list is None:
        return

    # Join the titles into a single string
    joined = ' '.join(hot_list)
    # Split the string into words, delimter == space character
    tokens = joined.split()

    # Ensure word_list is a unique list of lowercase words
    word_list = list(set([word.lower() for word in word_list]))

    # create an empty dictionary to store word: count pairs
    collection = {}

    # Count how many times a word in word_list appears in hot posts titles
    for word in word_list:
        for token in tokens:
            if word == token.lower():
                if word not in collection:
                    collection[word] = 0
                collection[word] += 1

    # Convert collection into a list of tuples
    pairs = list(collection.items())
    # Sort the list of tuples by words
    pairs.sort(key=lambda pair: pair[0])
    # Sort the list of tuples by count descending
    pairs.sort(key=lambda pair: pair[1], reverse=True)
    # Print the sorted count
    for pair in pairs:
        print('{}: {}'.format(pair[0], pair[1]))


def recurse(subreddit, after='', count=0, hot_list=[]):
    """
    Returns a list of titles of all hot posts of a subreddit

    Args:
        subreddit <str> : The subreddit to query
        after <str>     : Anchor point after which to get more posts
        count <int>     : Number of post items already seen
        hot_list <list> : A list to store all hot post titles
    Return:
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
