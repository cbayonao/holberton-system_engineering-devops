#!/usr/bin/python3
"""Write a function that queries the Reddit API
and returns the number of subscribers (not active
users, total subscribers) for a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """
    Method for retrieves number of subcribers of a subreddit
    """
    url = 'http://reddit.com/r/{}/about.json'
    headers = {'User-agent': 'custom'}
    r = requests.get(url.format(subreddit), headers=headers)
    if(r.status_code == 200):
        count = r.json().get("data").get("subscribers")
        return count
    else:
        return 0
