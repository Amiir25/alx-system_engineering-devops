#!/usr/bin/python3
'''
0-subs.py

This module contains a Python script that queries the Reddit API and returns
the number total subscribers.
'''

import requests


def number_of_subscribers(subreddit):
    '''
    Queries the Reddit API and returns the number of total subscribers
    for a given subreddit.
    '''

    url = (f"https://reddit.com/r/{subreddit}/about.json")
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MyRedditBot/1.0)"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)

    else:
        return 0
