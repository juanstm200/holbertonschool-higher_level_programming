#!/usr/bin/python3
""" script fetches """


import urllib.request


if __name__ == "__main__":
    re_html = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(re_html) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
