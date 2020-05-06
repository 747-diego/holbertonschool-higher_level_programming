#!/usr/bin/node
const noNum = 'Not a number';
const myNum = 'My number: ';
if (isNaN(parseInt(process.argv[2]))) {
  console.log(noNum);
} else {
  console.log(myNum + process.argv[2]);
}
