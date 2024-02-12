#!/usr/bin/node
const arglen = process.argv.length;

if (arglen >= 4) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
} else {
  console.log(process.argv[2] || 'undefined' + ' is ' + process.argv[3] || 'undefined');
}
