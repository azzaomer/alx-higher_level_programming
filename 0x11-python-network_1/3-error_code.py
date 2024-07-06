#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays the body of
the response (decoded in utf-8).
manage urllib.error.HTTPError exceptions and print: Error code
"""
from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError

if __name__ == "__main__":
    url = argv[1]
    rq = Request(url)
    try:
        with urlopen(url) as response:
            print(response.read().decode("ascii"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
