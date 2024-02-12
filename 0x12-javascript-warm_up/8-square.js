#!/usr/bin/node
const args = process.argv;
const str = 'X';
const x = parseInt(args[2], 10);

if (!isNaN(x) && x > 0) {
  for (let i = 0; i < x; i++) {
    let y = '';
    for (let j = 0; j < x; j++) {
      y = y + str;
    }
    console.log(y);
  }
} else console.log('Missing size');
