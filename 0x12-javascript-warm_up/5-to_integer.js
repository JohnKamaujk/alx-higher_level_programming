#!/usr/bin/node

const userInput = process.argv[2];

if (isNaN(userInput)) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(userInput));
}
