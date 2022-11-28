#!/usr/bin/node
const argv = require('node:process').argv;
const noArgu = argv.length;

if (noArgu === 2) {
  console.log('No argument');
} else if (noArgu === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
