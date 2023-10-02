#!/usr/bin/python3
'''takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.'''
import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    letter = argv[1] if len(argv) > 1 else ""
    data = {'q': letter}

    try:
        resp = requests.post(url, data)
        if resp.json():
            print("[{}] {}".format(resp.json()['id'], resp.json()['name']))
        else:
            print("No result")

    except Exception as exc:
        print("Not a valid JSON")
