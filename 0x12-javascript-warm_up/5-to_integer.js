#!/usr/bin/node

const lst = process.argv;
const num = parseInt(lst[2]);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
