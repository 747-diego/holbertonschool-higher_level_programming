#!/usr/bin/node
const second = parseInt(process.argv[2]);
function factorial (integer) {
  if (integer === 0 || isNaN(integer)) {
    return 1;
  }
  return integer * factorial(integer - 1);
}
console.log(factorial(second));
