#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  const numTasks = {};
  if (error) {
    console.log(error);
  } else {
	let  data = JSON.parse(body)
    for (const idx in data) {
      if (numTasks.completed === true) {
        if (!(numTasks.userId in numTasks)) {
          numTasks[data[idx].userId] = 1;
        } else {
          numTasks[data[idx].userId] += 1;
        }
      }
    }
    console.log(numTasks);
  }
});
