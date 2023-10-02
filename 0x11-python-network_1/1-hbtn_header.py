#!/usr/bin/python3
'''takes in a URL, sends a request to the URL and displays the value of
the X-Request-Id variable found in the header of the response.'''
import urllib.request as request
from sys import argv
if __name__ == "__main__":
    url = argv[1]

    try:
        with request.urlopen(url) as resp:
            print(resp.headers['X-Request-Id'])

    except Exception as exc:
        print(exc)
