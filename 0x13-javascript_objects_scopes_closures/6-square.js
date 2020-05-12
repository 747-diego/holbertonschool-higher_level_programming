#!/usr/bin/node
// Write a class Square that defines a square and inherits from 5-square.js
const Rectangle = require('./5-square');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  //   instance method that prints the rectangle using the character c
  charPrint (c) {
    c = 'X';
    for (let idx = 0; idx < this.height; idx++) {
      console.log(c.repeat(this.width));
    }
  }
};
