#!/usr/bin/node
const argv = require('node:process').argv;
let i = 2;

if (typeof (argv[2]) === 'undefined') {
  console.log('No argument');
} else {
  while (typeof (argv[i]) !== 'undefined') {
    console.log(argv[i]);
    i++;
  }
}
