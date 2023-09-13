#!/usr/bin/node
let dest = 0;

exports.logMe = function (item) {
  console.log(dest + ': ' + item);
  dest++;
};
