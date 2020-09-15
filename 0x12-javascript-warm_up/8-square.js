#!/usr/bin/node
let idx;
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (idx = 0; idx < size; idx++) {
    console.log('X'.repeat(size));
  }
}
