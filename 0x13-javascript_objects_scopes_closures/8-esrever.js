#!/usr/bin/node
// Write a function that returns the reversed version of a list:
exports.esrever = function (list) {
  const TemporaryList = [];
  let idx = list.length - 1;

  // Pushing the items in the old list into the new in reversed order
  while (idx >= 0) {
    TemporaryList.push(list[idx]);
    idx--;
  }

  return TemporaryList;
};
