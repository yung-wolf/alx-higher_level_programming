#!/usr/bin/node

function factorial (num) {
  if (num === 0 || num === 1 || isNaN(num)) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

const { argv } = require('node:process');
const arg1 = parseInt(argv[2]);

console.log(factorial(arg1));
