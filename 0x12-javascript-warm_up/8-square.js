#!/usr/local/bin/node

let col = parseInt(process.argv[2]);
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
