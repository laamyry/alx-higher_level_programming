#!/usr/bin/python3
'''takes your GitHub credentials (username and password) and uses
the GitHub API to display your id'''
import requests
from sys import argv
from requests.auth import HTTPBasicAuth
