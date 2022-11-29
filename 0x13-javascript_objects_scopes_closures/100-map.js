#!/usr/bin/node

const list = require('./100-data').list;
const list2 = list.map((v, i) => v * i);
console.log(list);
console.log(list2);
