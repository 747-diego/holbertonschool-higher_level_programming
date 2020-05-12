#!/usr/bin/node
// Write a class Square that defines a square and inherits from 4-rectangle.js
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
