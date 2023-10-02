#!/usr/bin/python3
'''takes your GitHub credentials (username and password) and uses
the GitHub API to display your id'''
import requests
from sys import argv
from requests.auth import HTTPBasicAuth as hba

if __name__ == "__main__":
    url = "https://api.github.com/user"

    try:
        resp = requests.get(url, auth=hba(argv[1], argv[2]))
        print(resp.json()['id'])

    except Exception as exc:
        print("None")
