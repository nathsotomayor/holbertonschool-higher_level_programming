#!/usr/bin/node
const array = process.argv;
let newArray;
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  newArray = array.slice(2);
  newArray.sort((a, b) => a - b);
  const arrSize = newArray.length;
  console.log(newArray[arrSize - 2]);
}
