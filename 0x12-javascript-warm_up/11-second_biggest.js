#!/usr/bin/node
// Script that searches for the second biggest integer
// in the list of arguments

if (process.argv.length <= 3) {
  console.log('0');
} else {
  // Convert the arguments to integers and store them in an array
  const args = process.argv.slice(2).map(Number);

  // Sort the array in descending order
  args.sort((a, b) => b - a);

  // The second biggest number will be the second item in the sorted array
  const maxTwo = args[1];

  console.log(maxTwo);
}
