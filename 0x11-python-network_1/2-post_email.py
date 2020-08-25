#!/usr/bin/python3
"""Sends a request to an URL and displays the value of the X-Request-Id"""

from urllib import request
import urllib.parse
import sys


if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        res = response.read()
        print(res.decode('utf-8'))
