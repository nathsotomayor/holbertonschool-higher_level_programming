#!/usr/bin/node
const sqr = require('./5-square');

class Square extends sqr {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let idx;
    for (idx = 1; idx <= this.height; idx++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
