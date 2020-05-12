#!/usr/bin/node
// Write a class Rectangle that defines a rectangle:
module.exports = class Rectangle {
    constructor (w, h) {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      }
    }
// instance method that prints the rectangle using the character X
    print () {
        for (let idx = 0; idx < this.height; idx++) {
          console.log('X'.repeat(this.width));
        }
      }
  };
