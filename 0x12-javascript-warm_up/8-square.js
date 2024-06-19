#!/usr/bin/node
// a script that prints a square

if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const size = Number(process.argv[2]);
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
