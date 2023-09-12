#!/usr/bin/node
const args = process.argv.slice(2);
const number1 = parseInt(args[0]);
const number2 = parseInt(args[1]);
if (isNaN(number1) || isNaN(num2)) {
  console.log("NaN");
} else {
  const result = number1 + num2;
  console.log(result);
}
