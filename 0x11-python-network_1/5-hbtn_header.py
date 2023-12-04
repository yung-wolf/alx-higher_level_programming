#!/usr/bin/python3

"""
module: 5-hbtn_header.py

Use request packages to fetch an https request
and displays the value of the variable X-Request-Id in the response header
"""

if __name__ == "__main__":

    import sys
    import requests

    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers['X-Request-Id'])
