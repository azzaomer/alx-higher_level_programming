#!/usr/bin/node
//  a function that returns the number of occurrences in a lis
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, current) => current === searchElement
    ? count + 1
    : count, 0
  );
};
