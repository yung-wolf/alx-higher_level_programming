#!/usr/bin/node

const { argv } = require('node:process');
const argvLen = argv.length;

if (argvLen === 2) {
  console.log('No argument');
} else {
  console.log(`${argv[2]}`);
}
