#!/usr/bin/node
// Write a script that imports an array and computes a new array.
const Old = require('./100-data.js').list;
console.log(Old);
console.log(Old.map((Value1, Value2) => Value1 * Value2));
