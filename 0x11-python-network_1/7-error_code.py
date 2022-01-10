#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response """


import requests
from sys import argv


if __name__ == '__main__':
    rq = requests.get(argv[1])
    if rq.status_code >= 400:
        print("Error code: {}".format(rq.status_code))
    else:
        print(rq.text)
