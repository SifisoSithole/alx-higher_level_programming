#!/usr/bin/node

function srt (b, c) {
  return (b - c);
}

let ints = process.argv;
if (ints.length === 2 || ints.length === 3) {
  console.log(0);
} else {
  ints = ints.slice(2);
  ints.forEach((ele, i) => {
    ints[i] = parseInt(ele);
  });
  ints.sort(srt);
  console.log(ints[ints.length - 2]);
}
