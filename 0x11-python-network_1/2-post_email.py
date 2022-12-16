#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST reques
t to the passed URL with the email as a parameter, and displays the bod
y of the response (decoded in utf-8)"""

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    from sys import argv as p
    m = urllib.parse.urlencode({'email': p[2]})
    m = m.encode("ascii")
    print(m)
    r = urllib.request.Request(p[1], m)
    with urllib.request.urlopen(r) as response:
        print(response.read().decode("utf-8"))
