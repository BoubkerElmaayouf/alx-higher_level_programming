#!/usr/bin/node
const { argv } = require('process');
const a = parseInt(argv[2], 10);
function factorial (x) {
  if (x <= 0) {
    return 1;
  }
  return x * factorial(x - 1);
}
if (isNaN(a)) console.log(1);
else console.log(factorial(a));
