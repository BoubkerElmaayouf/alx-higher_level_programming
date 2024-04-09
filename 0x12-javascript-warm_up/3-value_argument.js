#!/usr/bin/node
const [myarg] = process.argv.slice(2);

if (myarg) {
  console.log(myarg);
} else {
  console.log('No argument');
}
