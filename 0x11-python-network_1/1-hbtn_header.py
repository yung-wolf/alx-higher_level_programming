#!/usr/bin/python3

"""
module: 1-hbtn_header

Prints the X-Request-Id var of an http response
"""

if __name__ == "__main__":
    import sys
    import urllib.request

    url = sys.argv[1]
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        h_content = response.headers
        print(h_content['X-Request-Id'])
