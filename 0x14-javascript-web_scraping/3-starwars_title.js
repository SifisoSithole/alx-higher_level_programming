#!/usr/bin/node
// This script that prints the title of a Star Wars movie where the episode number matches a given integer.

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
const request = require('request');

request.get(url, (err, response, body) => {
  if (!err) {
    console.log(JSON.parse(body).title);
  }
});
