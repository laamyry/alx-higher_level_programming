#!/usr/bin/python3
'''takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8)'''
import urllib.request as request
import urllib.parse as parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = parse.urlencode({'email': email}).encode('utf-8')
    req = request.Request(url, data)
    try:
        with request.urlopen(req) as resp:
            print(resp.read().decode('utf-8'))
    except Exception as exc:
        print(exc)
