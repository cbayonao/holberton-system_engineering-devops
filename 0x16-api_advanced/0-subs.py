#!/usr/bin/python3
import requests
"""Write a function that queries the Reddit API
and returns the number of subscribers (not active
users, total subscribers) for a given subreddit."""


def number_of_subscribers(subreddit):
    """
    Method for retrieves number of subcribers of a subreddit
    """
    r = requests.get("https://reddit.com/r/{}/about.json".format(subreddit),
                     headers={"User-agent": "custom"})
    if(r.status_code == 200):
        return r.json().get("data").get("subscribers")
    return 0