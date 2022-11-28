#!/usr/bin/node

const lst = process.argv;
let str = 'X';
let i;

if (isNaN(lst[2])) {
  console.log('Missing size');
} else {
  const num = parseInt(lst[2]);
  for (i = 1; i < num; i++) {
    str += 'X';
  }

  for (i = 0; i < num; i++) {
    console.log(str);
  }
}
