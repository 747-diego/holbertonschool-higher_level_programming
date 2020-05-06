#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/* YOUR CODE HERE */

const increment = myObject.value;
myObject.incr = function () {
  increment++;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
