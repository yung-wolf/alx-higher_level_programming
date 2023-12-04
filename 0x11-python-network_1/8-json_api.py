#!/usr/bin/python3

"""
module: 8-json_api

Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

if __name__ == "__main__":

    def is_json_like(string):
        """ Check if string is JSON like"""
        try:
            # Attempt to evaluate the string as a Python expression
            eval_result = eval(string)

            # Check if the result is a dictionary (common for JSON-like str)
            return isinstance(eval_result, dict)
        except error as e:
            return False

    import sys
    import requests

    url = 'http://0.0.0.0:5000/search_user'
    q = ""

    # Take letter parameter from CLI
    if len(sys.argv) > 1:
        q = sys.argv[1]

    # check runs on integers and empty str but allows letters to pass quietly
    try:
        if not q or int(q):
            print("No result")
            sys.exit(0)
    except ValueError as err:
        error = err

    r = requests.post(url, data={'q': q})
    content = r.text

    # Take away braces & split by `,` & `\n`
    kv_pairs = content.replace('\n', '').strip('{}').split(',')
    data_id = kv_pairs[0][5:]
    name = kv_pairs[1][7:]
    name = name.strip('\"}')

    # If the response body is properly JSON formatted and not empty
    if content and is_json_like(content):
        data_id = int(data_id)
        print(f"{[data_id]} {name}")
    else:
        print("Not a valid JSON")
