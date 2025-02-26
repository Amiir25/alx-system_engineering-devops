#!/usr/bin/python3
'''
2-recurse.py

This module contains a Python script that queries the Reddit API and retuns
a list of titles of all hot articles
'''

import requests


def recurse(subreddit, hot_list=[], after=None):
    '''
    Recursively queries the Reddit API and returns a list containing the titles
    for a given subreddit or None if no resutls are found.
    '''

    url = (f"https://reddit.com/r/{subreddit}/about.json")
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MyRedditBot/1.0)"}
    params = {"limit": 100, "after": after} if after else {"limit": 100}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        hot_list.extend(post.get("data", {}).get("title") for post in posts)
        after = data.get("data", {}).get("after")

        if after:
            return recurse(subreddit, hot_list, after)

        return hot_list if hot_list else None

    else:
        print("None")
