#!/usr/bin/node
let index = 'No current occurence';
const second = process.argv[2];
if (isNaN(parseInt(second))) {
  console.log('Missing number of occurrences');
} else {
  for (index = 0; index < parseInt(second); index++) {
    console.log('C is fun');
  }
}
