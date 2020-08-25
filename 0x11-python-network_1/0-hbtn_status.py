#!/usr/bin/python3
"""Fetches url 'https://intranet.hbtn.io/status' with 'urllib'"""

from urllib import request


if __name__ == "__main__":
    req = request.Request('http://intranet.hbtn.io/status')
    with request.urlopen(req) as response:
        res = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(res)))
        print("\t- content: {}".format(res))
        print("\t- utf8 content: {}".format(res.decode('utf-8')))
