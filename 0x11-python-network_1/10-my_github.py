#!/usr/bin/python3

"""
module: 10-my_github

takes your GitHub credentials (username and password) and uses the
GitHub API to display your id
"""

if __name__ == "__main__":

    import sys
    import requests
    from requests.auth import HTTPBasicAuth

    # Take user & password args from CLI
    user = sys.argv[1]
    passwd = sys.argv[2]
    url = 'https://api.github.com/user'

    # Write Auth parameter
    basic = HTTPBasicAuth(user, passwd)

    response = requests.get(url, auth=basic)

    if response.status_code == 401:
        print('None')
    elif response.status_code == 200:
        user_data = response.json()
        print(user_data.get('id'))
