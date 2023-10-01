#!/usr/bin/python3
'''fetches https://alx-intranet.hbtn.io/status'''
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

try:
    with urllib.request.urlopen(url) as resp:
        content = resp.read()

        print('Body response:')
        print('\t- type: {}'.format(type(content)))
        print('\t- content: {}'.format(content))
        
except Exception as exc:
    print(exc)
