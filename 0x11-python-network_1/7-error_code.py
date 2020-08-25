#!/usr/bin/python3
"""Response header value with 'requests' package"""

import requests
import sys


if __name__ == "__main__":
    try:
        req = requests.get(sys.argv[1])
        print(req.text)
    except:
        print("Error code: {}".format(req.status_code))
