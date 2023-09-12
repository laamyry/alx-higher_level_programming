#!/usr/bin/node
const args = process.argv.slice(2).map(Number);
if (args.length > 1) {
  console.log(Math.max(...args.filter(num => num !== Math.max(...args))));
} else {
  console.log(0);
}