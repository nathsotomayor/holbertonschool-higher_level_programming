#!/usr/bin/node
let idx;
const num = parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (idx = 0; idx < num; idx++) {
    console.log('C is fun');
  }
}
