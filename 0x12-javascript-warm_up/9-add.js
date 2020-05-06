#!/usr/bin/node
const second = process.argv[2];
const third = process.argv[3];
function add (a, b) {
  return (parseInt(a) + parseInt(b));
}
console.log(add(second, third));
