#!/usr/bin/node

let arg1 = parseInt(process.argv[2]);

if (!isNaN(arg1)) {
  while (arg1 > 0) {
    console.log('C is fun');
    arg1--;
  }
} else {
  console.log('Missing number of occurrences');
}
