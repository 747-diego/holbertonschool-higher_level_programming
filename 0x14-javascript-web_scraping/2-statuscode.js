#!/usr/bin/node
// Write a script that display the status code of a GET request.
const GettingRequest = require('request');
const RequestingURL = process.argv[2];

GettingRequest
  .get(RequestingURL)
  .on('response', (response) => {
    console.log('code: ' + response.statusCode);
  });