#!/usr/bin/node

const SquareP = require('./5-square');

module.exports = class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let row = this.width;
      let col = this.height;

      const line = [];
      while (row > 0) {
        line.push('C');
        row--;
      }
      const lineString = line.join('');

      while (col > 0) {
        console.log(lineString);
        col--;
      }
    }
  }
};
