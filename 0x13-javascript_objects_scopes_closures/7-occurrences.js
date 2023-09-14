#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  let m = 0;
  while (m < list.length) {
    if (list[m] === searchElement) {
      count++;
    }
    m++;
  }
  return count;
};
