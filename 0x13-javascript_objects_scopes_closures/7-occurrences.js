#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach((v) => {
    if (v === searchElement) {
      count++;
    }
  });
  return (count);
};
