#!/usr/bin/node
let index = 'visible from outside';
exports.callMeMoby = function (x, theFunction) {
  for (index = 0; index < x; index++) {
    theFunction();
  }
};
