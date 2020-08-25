#!/usr/bin/python3
"""Fetches url 'https://intranet.hbtn.io/status' with 'urllib'"""

import urllib.request
with urllib.request.urlopen('http://intranet.hbtn.io/status') as response:
    res = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(res)))
    print("\t- content: {}".format(res))
    print("\t- utf8 content: {}".format(res.decode('utf-8')))
