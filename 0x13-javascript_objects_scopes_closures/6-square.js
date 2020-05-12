#!/usr/bin/node
// Write a class Square that defines a square and inherits from 4-rectangle.js
const Rectangle = require('./4-rectangle');
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
