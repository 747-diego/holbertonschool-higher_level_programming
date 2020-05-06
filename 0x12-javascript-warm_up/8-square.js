#!/usr/bin/node
const second = process.argv[2];
let size = 'empty';
if (isNaN(second)) {
  console.log('Missing size');
} else {
  for (size = 0; size < second; size++) {
    console.log('X'.repeat(second));
  }
}
