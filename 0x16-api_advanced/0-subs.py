#!/usr/bin/python3
"""
Get the subscribers count of a subreddit
"""
import requests
import time


def number_of_subscribers(subreddit):
    """
    Subreddit subscribers count
    """
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    headers = {"User-Agent": "Linux:v1.0.0 (Code Singer)"}
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        data = res.json()
        subs = data["data"]["subscribers"]
        return subs
    return 0
