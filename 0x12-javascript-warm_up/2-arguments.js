#!/usr/bin/node

const { argv } = require('node:process');
const argvLen = argv.length;

if (argvLen === 2) {
  console.log('No argument');
} else if (argvLen === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
