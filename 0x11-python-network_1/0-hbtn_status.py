#!/usr/bin/python3
'''fetches https://alx-intranet.hbtn.io/status'''
import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    try:
        with urllib.request.urlopen(url) as resp:
            content = resp.read()
            utf8_d = content.decode('utf-8')
            print("\t- type:", type(content))
            print("\t- content:", content)
            print("\t- utf8 content:", utf8_d)

    except Exception as exc:
        print(exc)
