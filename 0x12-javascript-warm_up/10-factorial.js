#!/usr/bin/node

function factorial (num) {
  if (num === 0 || num === 1 || isNaN(num)) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

const arg1 = parseInt(process.argv[2]);

console.log(factorial(arg1));
