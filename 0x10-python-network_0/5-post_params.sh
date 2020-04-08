#!/bin/bash
# akes in a URL, sends a POST request to the passed URL
curl -sd -XPOST '$1' 'email=hr@holbertonschool.com&subject=I will always be here for PLD'
