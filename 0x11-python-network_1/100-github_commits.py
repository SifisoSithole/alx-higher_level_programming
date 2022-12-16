#!/usr/bin/python3

if __name__ == '__main__':
    import requests
    from sys import argv as p
    url = "https://api.github.com/repos/{}/{}/commits".format(p[2], p[1])
    result = requests.get(url)
    try:
        d = result.json()
        for i in range(10):
            print("{}: {}".format(d[i]["sha"],
                                  d[i]["commit"]["author"]["name"]))
    except Exception:
        pass
