#!/usr/bin/python3

"""
module: 0-hbtn_status

Fetch https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.error

    url = 'https://alx-intranet.hbtn.io/status'

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            content = response.read()
            print("Body response:")
            print("\t- type:", type(content))
            print("\t- content:", content)
            print("\t- utf8 content:", content.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(e.reason)
        print(e.read())
