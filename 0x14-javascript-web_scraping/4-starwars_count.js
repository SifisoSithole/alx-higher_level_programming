#!/usr/bin/node
// This script that prints the number of movies where the character “Wedge Antilles” is present

const url = process.argv[2];
const request = require('request');
let noFilms = 0;

request.get(url, (err, response, body) => {
  if (!err) {
    const data = JSON.parse(body).results;
    for (const i in data) {
      data[i].characters.forEach((v) => {
        if (v.includes('18')) {
          noFilms++;
        }
      });
    }
    console.log(noFilms);
  }
});
