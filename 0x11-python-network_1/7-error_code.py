#!/usr/bin/python3
"""Print status code with 'requests' package"""

import requests
import sys


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    if req.status_code <= 400:
        print(req.text)
    else:
        print("Error code: {}".format(req.status_code))
