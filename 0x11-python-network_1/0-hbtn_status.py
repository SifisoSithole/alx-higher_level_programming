#!/usr/bin/python3
# This script fetches https://alx-intranet.hbtn.io/status

if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as rep:
        html = rep.read()
        print("Body response:")
        print(f'\t- type: {type(html)}')
        print(f'\t- content: {html}')
        print(f'\t- utf8 content: {html.decode("utf-8")}')

