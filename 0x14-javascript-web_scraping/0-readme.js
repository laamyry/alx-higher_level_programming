#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (er, data) => {
  if (er) {
    console.error(er);
  } else {
    console.log(data);
  }
});
