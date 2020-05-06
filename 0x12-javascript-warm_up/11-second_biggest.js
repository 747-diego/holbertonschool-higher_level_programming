#!/usr/bin/node
const Numbers = process.argv.length;
const BigNumTest = process.argv.slice(2);
if (Numbers < 4) {
  console.log(0);
} else {
  const CheckTest = BigNumTest.sort((a, b) => b - a);
  console.log(CheckTest[1]);
}
