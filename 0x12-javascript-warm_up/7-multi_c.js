#!/usr/bin/node

const lst = process.argv;

if (isNaN(lst[2])) {
  console.log('Missing number of occurrences');
} else {
  const num = parseInt(lst[2]);
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
