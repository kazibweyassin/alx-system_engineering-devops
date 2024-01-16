#!/usr/bin/python3
"""Returns a list containing the titles of all hot articles for a given subreddit"""
from requests import get
from sys import argv
import requests


def recurse(subreddit, hot_list=[]):
    """Returns a list containing the titles of all hot articles for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77\
               Safari/537.36'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        data = r.json()
        children = data.get("data").get("children")
        for child in children:
            hot_list.append(child.get("data").get("title"))
        after = data.get("data").get("after")
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list)
    else:
        return None
