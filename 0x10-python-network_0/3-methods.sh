#!/bin/bash
# Write a Bash script that takes in URL and displays all HTTP methods accepted
curl -sI '$1' | grep 'Allow' | cut -d' ' -f 2-
