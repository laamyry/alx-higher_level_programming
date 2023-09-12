#!/usr/bin/node
function callMeMoby (x, theFunction) {
  let m = 0;
  while (m < x) {
    theFunction();
    m++;
  }
}
module.exports = { callMeMoby };
