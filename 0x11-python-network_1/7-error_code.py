#!/usr/bin/python3

"""
module: 7-error_code

Python script that takes in a URL, sends a request to the URL and displays the
body of the response.
"""

if __name__ == "__main__":

    import sys
    import requests

    url = sys.argv[1]
    r = requests.get(url)
    status_c = r.status_code

    if (status_c > 399):
        print("Error code:", r.status_code)
    else:
        print(r.text)
