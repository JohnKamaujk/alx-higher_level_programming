#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const count = list.reduce((accumulator, currentValue) => {
    return currentValue === searchElement ? accumulator + 1 : accumulator;
  }, 0);

  return count;
};
