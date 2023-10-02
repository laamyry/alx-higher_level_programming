#!/usr/bin/python3
'''fetches https://alx-intranet.hbtn.io/status'''
import requests

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'

    try:
        resp = requests.get(url)
        print("Body response:")
        print("\t- type: {}".format(type(resp)))
        print("\t- content: {}".format(resp))
        print("\t- utf8 content: {}".format(resp))

    except Exception as exc:
        print(exc)
