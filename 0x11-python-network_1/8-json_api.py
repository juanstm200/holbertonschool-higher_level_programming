#!/usr/bin/python3
"""letter and sends a POST request to http://0.0.0.0:5000/search_user """


import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 2:
        letter = argv[1]
    else:
        letter = ""
    rq = requests.post('http://0.0.0.0:5000/search_user', data={'q': letter})

    try:
        rq = res.json()
        id = rq.get('id')
        name = rq.get('name')
        if len(rq) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(rq.get('id'), rq.get('name')))
    except Exception:
        print("Not a valid JSON")
