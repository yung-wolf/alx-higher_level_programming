#!/usr/bin/python3

"""
module: 3-error_code

Print the status code
"""

if __name__ == "__main__":
    import sys
    from urllib import parse, request, error

    url = sys.argv[1]

    req = request.Request(url)

    try:
        with request.urlopen(req) as response:
            content = response.read()
            print(content.decode('utf-8'))
    except error.HTTPError as e:
        print("Error code:", e.status)
