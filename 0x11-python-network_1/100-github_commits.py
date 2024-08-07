#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge.
"""

from sys import argv
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    rq = requests.get(url)
    commits = rq.json()

    try:
        for index in range(10):
            print("{}: {}".format(
                commits[index].get("sha"),
                commits[index].get("commit").get("author").get("name")))
    except IndexError:
        pass
