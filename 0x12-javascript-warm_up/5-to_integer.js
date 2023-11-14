#!/usr/bin/node

const { argv } = require('node:process');
const arg1 = parseInt(`${argv[2]}`);

if (!isNaN(arg1)) {
  console.log(`My number: ${arg1}`);
} else {
  console.log('Not a number');
}
