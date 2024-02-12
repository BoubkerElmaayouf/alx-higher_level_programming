#!/usr/bin/node
const args = process.argv.length;
const x = parseInt(process.argv[2]);
if (args !== 3) {
  console.log('Missing number of occurrences');
} else {
  if (!isNaN(x) && x > 0) {
    for (let i = 0; i < x; i++) {
      console.log('C is fun');
    }
  } else {
    console.log('Missing number of occurrences');
  }
}
