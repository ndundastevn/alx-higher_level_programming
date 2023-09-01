#!/usr/bin/python3
"""Fetche data from url  https://alx-intranet.hbtn.io/status."""
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        bodyy = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(bodyy)))
        print("\t- content: {}".format(bodyy))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
