#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};

let k = Object.keys(dict);
let v = Object.values(dict);
let n;
let l;
let index;

while (v.length !== 0) {
  l = [];
  l.push(k.pop());
  n = v.pop();
  while (v.includes(n)) {
    index = v.indexOf(n);
    l.push(k[index]);
    v = v.slice(0, index).concat(v.slice(index + 1));
    k = k.slice(0, index).concat(k.slice(index + 1));
  }
  newDict[n] = l;
}
console.log(newDict);
