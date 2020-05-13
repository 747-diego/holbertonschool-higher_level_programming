#!/usr/bin/node
// Write a script that gets the contents of a webpage and stores it in a file.
const fs = require('fs');
const GettingRequest = require('request');
const content = process.argv;

GettingRequest(content[2], (err, res, body) => {
  if (err) {
    console.log(err);
  }

  fs.writeFile(content[3], body, (err) => {
    if (err) {
      console.log(err);
    }
  });
});
