#!/usr/bin/node
exports.esrever = function (list) {
  const reversedlist = [];
  for (let m = list.length - 1; m => 0; m--) {
    reversedlist.push(list[m]);
  }
  return reversedlist;
};
