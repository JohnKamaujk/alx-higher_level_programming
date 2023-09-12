#!/usr/bin/node
const SquareA = require('./5-square');

class Square extends SquareA {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const symbol = c === undefined ? 'X' : c;

    for (let i = 0; i < this.height; i++) {
      console.log(`${symbol}`.repeat(this.width));
    }
  }
}

module.exports = Square;
