#!/usr/bin/node
const SquareBase = require('./5-square');

class Square extends SquareBase {
  charPrint(c = 'X') {
    let m = 0;
    while ( m < this.height) {
      console.log(c.repeat(this.width));
      m++;
    }
  }
}
module.exports = Square;
