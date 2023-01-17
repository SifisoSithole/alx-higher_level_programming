#!/usr/bin/node
// This script that prints all characters of a Star Wars movie

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
const request = require('request');

request.get(url, (err, resp, body) => {
  if (!err) {
    const characters = JSON.parse(body).characters;
    for (const i in characters) {
      const url2 = characters[i].substring(0, characters[i].length - 1);
      request.get(url2, (e, res, b) => {
        if (!e) {
          while (!res && res.statusCode !== 200) {
            continue;
          }
          console.log(JSON.parse(b).name);
        }
      });
    }
  }
});
