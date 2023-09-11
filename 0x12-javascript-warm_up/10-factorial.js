#!/usr/bin/node

function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

if (isNaN(process.argv[2])) {
  console.log(1);
} else {
  const value = parseInt(process.argv[2]);
  const answer = factorial(value);
  console.log(answer);
}
