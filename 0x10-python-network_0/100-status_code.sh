#!/bin/bash
# Sends a GET request to a given URL and display the response status code of response.
curl -s -o /dev/null -w "%{http_code}" "$1"
