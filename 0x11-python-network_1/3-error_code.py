#!/usr/bin/python3
"""Manage 'urllib.error.HTTPError' exceptions and print: 'Error code:' followed
by the HTTP status code"""

from urllib import request
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    req = request.Request(sys.argv[1])
    try:
        with request.urlopen(req) as response:
            res = response.read()
            print(res.decode('utf-8'))
    except HTTPError as err_code:
        print("Error code: {}".format(err_code.code))
