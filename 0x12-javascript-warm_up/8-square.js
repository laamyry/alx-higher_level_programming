#!/usr/bin/node
const args = process.argv.slice(2);
const size = parseInt(args[0]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let m = 0; m < size; m++) {
    let row = '';
    for (let n = 0; n < size; n++) {
      row += 'X';
    }
    console.log(row);
  }
}
