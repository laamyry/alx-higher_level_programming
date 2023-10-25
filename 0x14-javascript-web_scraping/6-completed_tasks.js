#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
request(url, function (er, resp, body) {
  if (er) {
    console.log(er);
  } else if (resp.statusCode === 200) {
    const completed = {};
    const tsks = JSON.parse(body);
    for (const m in tsks) {
      const tsk = tsks[m];
      if (tsk.completed === true) {
        if (completed[tsk.userId] === undefined) {
          completed[tsk.userId] = 1;
        } else {
          completed[tsk.userId]++;
        }
      }
    }
    console.log(completed);
  }
});
