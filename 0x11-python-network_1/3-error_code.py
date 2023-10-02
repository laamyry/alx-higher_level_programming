#!/usr/bin/python3
''' takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).'''
import urllib.request as request
import urllib.error as error
from sys import argv

if __name__ == "__main__":
    url = argv[1]

    try:
        with request.urlopen(url) as resp:
            content = resp.read()
            utf8_d = content.decode('utf-8')
            print(utf8_d)

    except error.HTTPError as err:
        print("Error code: {}".format(err.code))