#!/usr/bin/node
const argslen = process.argv.length;

if (argslen === 2) {
  console.log('No argument');
}

for (let i = 2; i < argslen; i++) {
  console.log(process.argv[i]);
}
