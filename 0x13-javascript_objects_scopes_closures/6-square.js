#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const symbol = c === undefined ? 'X' : c;

    for (let i = 0; i < this.height; i++) {
      console.log(symbol.repeat(this.width));
    }
  }
}

module.exports = Square;
