#!/usr/bin/node
// script that prints x C is
const x = parseInt(process.argv[2]);
if (x) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
