#!/usr/bin/node
// Write a script that reads and prints the content of a file.
const fs = require('fs');
const content = process.argv;

fs.readFile(content[2], 'utf-8', (err, NoErr) => {
  if (err) {
    console.log(err);
  } else {
    console.log(NoErr);
  }
});
