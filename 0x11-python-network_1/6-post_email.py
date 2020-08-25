#!/usr/bin/python3
"""Response header value with 'requests' package"""

import requests
import sys


if __name__ == "__main__":
    value = {'email': sys.argv[2]}
    req = requests.get(sys.argv[1], data=value)
    print(req)
