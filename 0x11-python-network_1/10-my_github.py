#!/usr/bin/python3
"""Check status"""


if __name__ == '__main__':
    import requests
    from requests.auth import HTTPBasicAuth
    from sys import argv as p
    result = requests.get("https://api.github.com/user",
                          auth=(HTTPBasicAuth(p[1], p[2])))

    try:
        data = result.json()
        print(data["id"])
    except Exception:
        print("None")
