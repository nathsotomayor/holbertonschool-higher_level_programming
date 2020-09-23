#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  let count = 0;
  if (error) {
    console.log(error);
  }
  for (const film of JSON.parse(body).results) {
    count += film.characters.filter(each => each.search('/18/') > 0).length;
  }
  console.log(count);
});
