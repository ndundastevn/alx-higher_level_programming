#!/usr/bin/python3
import sys
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    data = response.read()
    print(data)
    
