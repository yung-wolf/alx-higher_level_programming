#!/usr/bin/node

exports.esrever = function (list) {
  const listLen = list.length;
  const revList = [];
  let i = 0;

  while (i < listLen) {
    revList.push(list.pop());
    i++;
  }

  return revList;
};
