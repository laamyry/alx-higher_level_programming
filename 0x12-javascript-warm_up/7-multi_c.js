#!/usr/bin/node
let m = 0;
const arg = parseInt(process.argv[2]);
if (!isNaN(arg) && arg > 0) {
  while (m < arg) {
    console.log("C is fun");
    m++;
  }
} else {
  console.log("Missing number of occurrences");
}