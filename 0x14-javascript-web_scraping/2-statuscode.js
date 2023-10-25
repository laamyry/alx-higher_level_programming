#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (er, resp) => {
  if (er) {
    console.error(er);
  } else {
    console.log(`code: ${resp.statusCode}`);
  }
});
