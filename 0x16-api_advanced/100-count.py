#!/usr/bin/python3
'''
100-count.py

This module contains a Python script that recursively queries the Reddit
API, parses the title of all hot articles, and prints a sorted count of
given keywords
'''
from collections import Counter
import re
import requests


def count_words(subreddit, word_list, counts=None, after=None):
    """
    Recursively queries the Reddit API, parses the title of all hot
    articles, and prints a sorted count of given keywords
    (case-insensitive, space-delimited).

    Words are counted individually, ignoring punctuation but keeping exact
    word matches.
    """
    if counts is None:
        counts = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MyRedditBot/1.0)"}
    params = {"limit": 100, "after": after} if after else {"limit": 100}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])

        word_list = [word.lower() for word in word_list]
        pattern = re.compile(r'\b\w+\b')

        for post in posts:
            title_words = pattern.findall(post.get(
                "data", {}).get("title", "").lower()
            )
            filtered_words = [
                word for word in title_words if word in word_list
            ]
            counts.update(filtered_words)

        after = data.get("data", {}).get("after")
        if after:
            return count_words(subreddit, word_list, counts, after)

        sorted_counts = sorted(
            counts.items(), key=lambda x: (-x[1], x[0])
        )
        for word, count in sorted_counts:
            print(f"{word}: {count}")
