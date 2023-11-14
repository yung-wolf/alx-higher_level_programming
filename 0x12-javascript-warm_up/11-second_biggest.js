#!/usr/bin/node

const { argv } = require('node:process');
const argvLen = argv.length;

if (argvLen === 2 || argvLen === 3) {
  console.log(0);
} else {
  let secondBigNum = 0;
  let biggestNum = parseInt(argv[2]);

  argv.forEach((val, index) => {
    if (parseInt(val) > biggestNum) {
      secondBigNum = biggestNum;
      biggestNum = parseInt(val);
    } else if (parseInt(val) > secondBigNum) {
      secondBigNum = parseInt(val);
    }
  });

  console.log(`${secondBigNum}`);
}
