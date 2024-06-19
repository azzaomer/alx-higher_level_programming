#!/usr/bin/node

if (process.argv.length === 2 || isNaN(process.argv[2])) {
  console.log('0');
} else {
  let max = process.argv[1];
  let maxTwo = process.argv[2];
  for (let i = 0; i < process.argv.length; i++) {
    if (process.argv[i] > max) {
      max = process.argv[i];
    }
  }
  for (let j = 0; j < process.argv.length; j++) {
    if (process.argv[j] > maxTwo && process.argv[j] !== max) {
      maxTwo = process.argv[j];
    }
  }
  console.log(maxTwo);
}
