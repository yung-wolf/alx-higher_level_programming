#!/usr/bin/python3

"""
module: 2-post_email

Python script that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the body of
the response (decoded in utf-8)
"""

if __name__ == "__main__":
    import sys
    from urllib import parse, request

    url = sys.argv[1]
    email = sys.argv[2]

    # Pass and encode email as URL parameter
    data = parse.urlencode({'email': email})
    data = data.encode('utf-8')
    req = request.Request(url, data)

    with request.urlopen(req) as response:
        content = response.read()
        print(content.decode('utf-8'))
