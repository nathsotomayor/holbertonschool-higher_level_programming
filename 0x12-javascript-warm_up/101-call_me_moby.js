#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let idx = 0; idx < x; idx++) {
    theFunction();
  }
};
