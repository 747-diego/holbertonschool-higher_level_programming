#!/bin/bash
# Write a Bash script that takes in a URL and sends requests the body size
curl -sI "$1" | grep "Content-Length" | cut -d " " -f 2
