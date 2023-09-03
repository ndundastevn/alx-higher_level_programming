#!/usr/bin/python3
"""akes a letter as an argument and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    req = requests.post("http://0.0.0.0:5000/search_user", data={'q': letter}
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
