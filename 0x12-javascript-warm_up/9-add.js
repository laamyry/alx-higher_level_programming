#!/usr/bin/node
function add (a, b) {
  const number1 = parseInt(a);
  const number2 = parseInt(b);

  if (isNaN(number1) || isNaN(number2)) {
    console.log('NaN');
  } else {
    console.log(number1 + number2);
  }
}

const arg1 = process.argv[2];
const arg2 = process.argv[3];

add(arg1, arg2);
