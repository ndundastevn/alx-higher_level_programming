#!/bin/bash
#accept URL as an urgumnt and displays all HTTP methods the server will accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
