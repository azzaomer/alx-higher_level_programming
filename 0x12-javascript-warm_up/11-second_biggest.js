#!/usr/bin/node
// script that searches the second biggest
// integer in the list of arguments
if (process.argv.length <= 3) {
  console.log('0');
} else {
  let max = process.argv[2];
  let maxTwo = process.argv[3];
  for (let i = 3; i < process.argv.length; i++) {
    if (process.argv[i] > max) {
      max = process.argv[i];
    }
  }
  console.log(`The first max = ${max}`)
  console.log(`Initaial max 2 = ${maxTwo}`)
  for (let j = 2; j < process.argv.length; j++) {
    console.log(`argument ${j}: ` +  process.argv[j])
    if (process.argv[j] > maxTwo && process.argv[j] !== max) {
      maxTwo = process.argv[j];
      console.log(`the second bigest: ` + process.argv[j])
    }
  }
  console.log(maxTwo);
}
