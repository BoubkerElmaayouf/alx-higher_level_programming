#!/usr/bin/node
function add (a, b) {
  return parseInt(a) + parseInt(b);
}
const args = process.argv;
const res = add(args[2], args[3]);
console.log(res);
