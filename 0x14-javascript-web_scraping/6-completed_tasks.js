#!/usr/bin/node
// This script that computes the number of tasks completed by user id

const url = process.argv[2];
const request = require('request');

request(url, (err, response, body) => {
  if (!err) {
    const todos = JSON.parse(body);
    const userId = [];
    const completed = [];
    let ind = 0;
    for (const i in todos) {
      if (userId.includes(todos[i].userId)) {
        if (todos[i].completed) {
          ind = userId.indexOf(todos[i].userId);
          completed[ind]++;
        }
      } else {
        if (todos[i].completed) {
          userId.push(todos[i].userId);
          completed.push(1);
        }
      }
    }
    const results = {};
    for (const i in completed) {
      results[userId[i]] = completed[i];
    }
    console.log(results);
  }
});
