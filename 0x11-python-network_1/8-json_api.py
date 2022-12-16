#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
if __name__ == '__main__':
    import requests
    from sys import argv as p

    if len(p) == 1:
        p = {'q': ''}
    else:
        p = {'q': p[2]}

    res = requests.post('http://0.0.0.0:5000/search_user', p)
    try:
        r = res.json()
        if r:
            print("[{}] {}".format(data["id"], data["name"]))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
