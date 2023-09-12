#!/usr/bin/node
let x = 0;
const arg = parseInt(process.argv[2]);
if (!isNaN(arg) && arg > 0) {
  while (x < arg) {
    console.log('C is fun');
    x++;
  }
} else {
  console.log('Missing number of occurrences');
}
