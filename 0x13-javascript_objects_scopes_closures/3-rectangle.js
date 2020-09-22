#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let idx;
    for (idx = 1; idx <= this.height; idx++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
