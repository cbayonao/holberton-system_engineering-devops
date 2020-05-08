#!/usr/bin/python3
"""Function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a
given subreddit."""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts
    """
    r = requests.get("https://reddit.com/r/{}.json?sort=hot&limit=10".
                     format(subreddit), headers={"User-agent": "custom"})

    if(r.status_code == 200):
        for subred in r.json().get("data").get("children"):
            print(subred.get("data").get("title"))
    else:
        print("None")
