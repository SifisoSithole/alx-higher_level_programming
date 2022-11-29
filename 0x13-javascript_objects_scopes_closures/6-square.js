#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let chr = '';

    if (typeof (c) === 'undefined') {
      c = 'X';
    }

    for (let i = 0; i < this.width; i++) {
      chr += c;
    }

    for (let i = 0; i < this.width; i++) {
      console.log(chr);
    }
  }
}
module.exports = Square;
