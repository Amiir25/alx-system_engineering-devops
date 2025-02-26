#!/usr/bin/python3
'''
1-top_ten.py

This module contains a Python script that queries the Reddit API and prints
the titles of the first 10 hot posts.
'''

import requests


def top_ten(subreddit):
    '''
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    '''

    url = (f"https://reddit.com/r/{subreddit}/about.json")
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MyRedditBot/1.0)"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])

        for post in posts:
            print(post.get("data", {}).get("title"))

    else:
        print(None)
