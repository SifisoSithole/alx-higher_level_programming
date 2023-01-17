#!/usr/bin/node
// This script that gets the contents of a webpage and stores it in a file.

const url = process.argv[2];
const file = process.argv[3];
const request = require('request');
const fs = require('fs');

request(url).pipe(fs.createWriteStream(file));
