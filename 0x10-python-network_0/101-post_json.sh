#!/bin/bash
# a JSON POST request to a URL passed as the first argument
curl -sH -XPOST 'Content-Type: application/json' -d '@$2' '$1'
