#!/usr/bin/node
// Write a script that writes a string to a file.
const fs = require('fs');
const content = process.argv;

fs.writeFile(content[2], content[3], 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
