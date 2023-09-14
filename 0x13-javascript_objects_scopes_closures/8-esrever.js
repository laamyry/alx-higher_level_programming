#!/usr/bin/node
exports.esrever = function (list) {
  const reversedlist = [];
  let m = list.length - 1;
  while (m >= 0) {
    reversedlist.push(list[m]);
    m--;
  }
  return reversedlist;
};
