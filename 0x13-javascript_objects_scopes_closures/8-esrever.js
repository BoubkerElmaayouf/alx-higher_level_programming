#!/usr/bin/node
exports.esrever = function (list) {
  const emptyList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    emptyList.push(list[i]);
  }
  return emptyList;
};
