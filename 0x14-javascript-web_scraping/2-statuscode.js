#!/usr/bin/node
const request = require('request');

const url = process.argv[1];

request(url, (er, response) => {
  if (er) {
    console.error(er);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
