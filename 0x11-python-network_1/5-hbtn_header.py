#!/usr/bin/python3
""" sends a request to the URL and displays the value """


import requests
from sys import argv


if __name__ == "__main__":
    rq = requests.get(argv[1])
    print(rq.headers.get('X-Request-Id'))
