#!/usr/bin/node
// Write a function that returns the number of occurrences in a list:
exports.nbOccurences = function (list, searchElement) {
  let Occurrences = 0;
  for (let idx = 0; idx < list.length; idx++) {
    if (list[idx] === searchElement) {
      Occurrences++;
    }
  }
  return Occurrences;
};
