#!/usr/bin/node
const data = require('./101-data');
const initDict = data.dict;
const newdict = {};

for (const id in initDict) {
  const occr = initDict[id];
  if (!newdict[occr]) {
    newdict[occr] = [];
  }
  newdict[occr].push(id);
}
console.log(newdict);
