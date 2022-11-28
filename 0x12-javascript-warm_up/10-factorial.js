#!/usr/bin/node

function fctoril (n) {
  if (isNaN(n) || n < 1) {
    return (1);
  } else {
    return (n * fctoril(n - 1));
  }
}

console.log(fctoril(process.argv[2]));
