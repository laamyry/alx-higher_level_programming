#!/usr/bin/python3
'''takes in a URL and an email address, sends a POST request to
the passed URL with the email as a parameter, and finally displays
the body of the response.'''
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    mail = argv[2]
    data = {'email': mail}
    
    try:
        resp = requests.post(url, data)
        print(resp.text)

    except Exception as exc:
        print(exc)