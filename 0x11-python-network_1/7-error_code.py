#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and
displays the body of the response.
"""

if __name__ == '__main__':
    import requests
    from sys import argv as p

    r = requests.get(p[1])
    try:
        if r.status_code == requests.codes.ok:
            print(r.text)
        else:
            print(f'Error code: {r.status_code}')
    except Exception:
        pass
