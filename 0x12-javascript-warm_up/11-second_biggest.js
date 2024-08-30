#!/usr/bin/node
// script that searches the second biggest
// integer in the list of arguments
if (process.argv.length <= 3) {
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
