#!/usr/bin/node
const S = require('./5-square');

class Square extends S {
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
