#!/usr/bin/node

if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  let secondBigNum = -1000;
  let biggestNum = parseInt(process.argv[2]);

  process.argv.forEach((val, index) => {
    if (parseInt(val) > biggestNum) {
      secondBigNum = biggestNum;
      biggestNum = parseInt(val);
    } else if (parseInt(val) > secondBigNum) {
      secondBigNum = parseInt(val);
    }
  });

  console.log(`${secondBigNum}`);
}
