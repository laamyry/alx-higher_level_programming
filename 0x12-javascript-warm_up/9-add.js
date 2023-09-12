#!/usr/bin/node
function add(a, b) {
    return a + b;
  }
  
  const args = process.argv.slice(2);
  const number1 = parseInt(args[0]);
  const number2 = parseInt(args[1]);
  
  if (isNaN(number1) || isNaN(number2)) {
    console.log("NaN");
  } else {
    const result = add(number1, number2);
    console.log(result);
  }
