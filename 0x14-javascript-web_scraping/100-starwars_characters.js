#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (er, resp, body) {
  if (!er) {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      request(character, function (er, resp, body) {
        if (!er) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
