#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  /* print the Rectangle object */
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

  /* Rotates the rectangle obj (swaps `w` & `h`) */
  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  /* Double the width & height values */
  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
