#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let chr = '';
    for (let i = 0; i < this.width; i++) {
      chr += 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(chr);
    }
  }
}

module.exports = Rectangle;
