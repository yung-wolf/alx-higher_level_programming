#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let row = this.width;
    let col = this.height;

    const line = [];
    while (row > 0) {
      line.push('X');
      row--;
    }
    const lineString = line.join('');

    while (col > 0) {
      console.log(lineString);
      col--;
    }
  }
};
