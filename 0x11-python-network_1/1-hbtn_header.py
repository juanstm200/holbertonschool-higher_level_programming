#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status """


import urllib.request as request
from sys import argv


if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        print(response.getheader('X-Request-Id'))
