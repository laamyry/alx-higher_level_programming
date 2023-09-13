#!/usr/bin/node
const {list} = require('./100-data');
const new_List = list.map((value, index) => value * index);
console.log(new_List);