#!/bin/bash
# makes a request to a server and responds with a message: 'You got me!'
curl -sLH -XPUT 'Origin: HolbertonSchool' -d 'user_id=98'  0.0.0.0:5000/catch_me
