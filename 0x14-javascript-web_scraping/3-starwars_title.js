#!/usr/bin/node
const request = require('request');

const movieid = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieid}`;

request.get(url, (er, resp, body) => {
  if (er) {
    console.log(er);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
