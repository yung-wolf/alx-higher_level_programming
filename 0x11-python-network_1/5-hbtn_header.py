#!/usr/bin/python3

"""
module: 5-hbtn_header.py

Use request packages to fetch an https request
and displays the value of the variable X-Request-Id in the response header
"""

if __name__ == "__main__":

    import requests

    r = requests.get('https://alx-intranet.hbtn.io/status')
    print(r.headers['X-Request-Id'])
