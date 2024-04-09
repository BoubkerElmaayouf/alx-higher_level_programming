#!/usr/bin/node
const args = process.argv[2];
const isnum = parseInt(args);

if (isNaN(isnum)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + isnum);
}
