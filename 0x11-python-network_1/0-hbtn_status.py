#!/usr/bin/python3
'''fetches https://alx-intranet.hbtn.io/status'''
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

try:
    with urllib.request.urlopen(url) as resp:
        content = resp.read()
        utf8_d = content.decode('utf-8')
        print("    - type:", type(content))
        print("    - content:", content)
        print("    - utf8 content:", utf8_d)

except Exception as exc:
    print(exc)
