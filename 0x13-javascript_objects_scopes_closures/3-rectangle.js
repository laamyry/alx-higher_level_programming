#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 || h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let m = 0;
    while (m < this.height) {
      console.log('X'.repeat(this.width));
      m++;
    }
  }
}

module.exports = Rectangle;
