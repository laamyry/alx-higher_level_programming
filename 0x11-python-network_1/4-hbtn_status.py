#!/usr/bin/python3
'''fetches https://alx-intranet.hbtn.io/status'''
import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    try:
        resp = requests.get(url)
        print("Body response:")
        print("\t- type: {}".format(type(resp.text)))
        print("\t- content: {}".format(resp.text))

    except Exception as exc:
        print(exc)
