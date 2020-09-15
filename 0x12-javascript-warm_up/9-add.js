#!/usr/bin/node
function add (a, b) {
  let sum;
  a = parseInt(process.argv[2]);
  b = parseInt(process.argv[3]);
  sum = a + b;
  return sum;
}
console.log(add());
