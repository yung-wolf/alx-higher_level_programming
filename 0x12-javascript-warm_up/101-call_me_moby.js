#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < 3; i++) {
    theFunction();
  }
};
