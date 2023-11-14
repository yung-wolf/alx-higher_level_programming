#!/usr/bin/node

const { argv } = require('node:process');
let col = parseInt(`${argv[2]}`);
let row = col;

if (!isNaN(col)) {
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
} else {
  console.log('Missing size');
}
