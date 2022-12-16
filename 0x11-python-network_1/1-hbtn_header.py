#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in the header
of the response."""

if __name__ == '__main__':
    import urllib.request
    from sys import argv as p
    with urllib.request.urlopen(p[1]) as response:
        h = response.info()
        print(h['X-Request-Id'])
