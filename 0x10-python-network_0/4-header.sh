#!/bin/bash
# takes in a URL as an argument, sends GET request to the URL, display response
curl -sH -XGET '$1' 'X-HolbertonSchool-User-Id: 98'
