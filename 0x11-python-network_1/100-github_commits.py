#!/usr/bin/python3
""" takes 2 arguments in order to solve this challenge."""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth as hba

if __name__ == "__main__":
    url = "https://api.github.com/user"
