#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;

  for (const e of list) {
    if (e === searchElement) {
      counter++;
    }
  }
  return counter;
};
