#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response """


import urllib.error as err
import urllib.request as request
from sys import argv


if __name__ == "__main__":
    r = request.Request(argv[1])
    try:
        with request.urlopen(r) as rq:
            print(rq.read().decode('utf-8'))
    except err.HTTPError as e:
        print("Error code: {}".format(e.code))
