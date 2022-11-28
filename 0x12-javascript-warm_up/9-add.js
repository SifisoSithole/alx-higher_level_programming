#!/usr/bin/node

function add (a, b) {
  if (isNaN(a) && isNaN(b)) {
    return (NaN);
  } else {
    return (parseInt(a) + parseInt(b));
  }
}

const lst = process.argv;
console.log(add(lst[2], lst[3]));
