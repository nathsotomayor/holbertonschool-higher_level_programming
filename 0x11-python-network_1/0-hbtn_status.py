#!/usr/bin/python3
"""Fetches url 'https://intranet.hbtn.io/status' with 'urllib'"""

import urllib.request
with urllib.request.urlopen('http://intranet.hbtn.io/status') as response:
    html = response.read()
    print("""Body response:
    - type: {}
    - content: {}
    - utf8 content: {}""".
          format(type(html), html, html.decode('utf-8')))
    # print(type(html))
    # print(html)
    # print(html.decode('utf-8'))
