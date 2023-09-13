#!/usr/bin/node
const fs = require('fs');
const [src1, src2] = process.argv.slice(2);
fs.writeFileSync(fs.readFileSync(src1) + fs.readFileSync(src2));
