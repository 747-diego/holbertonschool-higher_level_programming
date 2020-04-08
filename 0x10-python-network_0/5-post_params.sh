#!/bin/bash
# akes in a URL, sends a POST request to the passed URL
curl -s -XPOST "$1" -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
