#!/usr/bin/python3
'''takes in a URL, sends a request to the URL and displays the value of
the X-Request-Id variable found in the header of the response.'''
import urllib.request as request
import sys

if __name__ == "__main__":
    url = sys.argv[0]

    try:
        with request.urlopen(url) as resp:
            print(resp.headers['X-Request-Id'])

    except Exception as exc:
        print(exc)
