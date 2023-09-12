#!/usr/bin/node
const data = require('./101-data.js').dict;

const userIdsByOccurrence = {};

for (const userId in data) {
  const occurrence = data[userId];

  if (occurrence in userIdsByOccurrence) {
    userIdsByOccurrence[occurrence].push(userId);
  } else {
    userIdsByOccurrence[occurrence] = [userId];
  }
}

console.log(userIdsByOccurrence);
