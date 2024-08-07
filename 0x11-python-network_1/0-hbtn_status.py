#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
from urllib.request import Request, urlopen

if __name__ == "__main__":
    rq = Request("https://alx-intranet.hbtn.io/status")
    with urlopen(rq) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
