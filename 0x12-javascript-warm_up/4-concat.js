#!/usr/bin/node
const det = ' is ';
const [arg1, arg2] = process.argv.slice(2);

console.log((arg1 || 'undefined') + det + (arg2 || 'undefined'));
