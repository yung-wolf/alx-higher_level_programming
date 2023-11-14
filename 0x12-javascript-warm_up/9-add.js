#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const { argv } = require('node:process');
const arg1 = parseInt(argv[2]);
const arg2 = parseInt(argv[3]);

console.log(add(arg1, arg2));
