#!/usr/bin/python3
"""Sends a request to an URL and displays the value of the X-Request-Id"""

from urllib import request
import sys


if __name__ == "__main__":
    req = request.Request(sys.argv[1])
    with request.urlopen(req) as response:
        res = response.headers['X-Request-Id']
        print(res)
