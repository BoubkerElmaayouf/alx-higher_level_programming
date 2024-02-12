#!/usr/bin/node
const args = process.argv[2];
const parsingNum = parseInt(args);

if (isNaN(parsingNum)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parsingNum}`);
}
