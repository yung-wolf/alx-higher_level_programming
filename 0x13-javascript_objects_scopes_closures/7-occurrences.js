#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const listLen = list.length - 1;
  let count = 0;

  for (let i = 0; i <= listLen; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }

  return count;
};
