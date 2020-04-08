#!/bin/bash
# takes in a URL as an argument, sends GET request to the URL, display response
curl -s -XGET "$1" -H "X-HolbertonSchool-User-Id: 98"
