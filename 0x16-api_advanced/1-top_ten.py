#!/usr/bin/python3
""" Module that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit. """
from requests import get
import requests

def top_ten(subreddit):
    """ Prints the titles of the first 10 posts of a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 19.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    else:
        print("None")
