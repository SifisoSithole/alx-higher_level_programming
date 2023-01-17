#!/usr/bin/node
// This script that display the status code of a GET request

const url = process.argv[2];
const request = require('request');

request.get(url, (err, response, body) => {
  if (!err) {
    	console.log('code:', response.statusCode);
  }
});
