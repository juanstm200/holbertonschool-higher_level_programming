#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status """


import requests


if __name__ == "__main__":
    solicitud = requests.get('https://intranet.hbtn.io/status')
    text = solicitud.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
