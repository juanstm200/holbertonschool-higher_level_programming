#!/usr/bin/python3
""" sends a POST request to http://0.0.0.0:5000/search_user """


import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    rq = requests.get(url, auth=HTTPBasicAuth(argv[1], argv[2]))
    print(rq.json().get('id'))
