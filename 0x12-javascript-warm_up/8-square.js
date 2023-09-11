#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const times = parseInt(process.argv[2]);

  for (let i = 0; i < times; i++) {
    console.log('X'.repeat(times));
  }
}
