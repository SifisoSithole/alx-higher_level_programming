#!/usr/bin/node
// script that writes a string to a file

if (process.argv.length === 4) {
  const file = process.argv[2];
  const str = process.argv[3];
  const fs = require('fs');

  fs.writeFile(file, str, err => {
    if (err) {
      console.log(err);
    }
  });
}
