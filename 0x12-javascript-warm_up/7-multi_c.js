#!/usr/bin/node

<<<<<<< HEAD
function factorial (n) {
    if (n < 0) {
        return (-1);
    }
    if (n === 0 || isNaN(n)) {
        return (1);
    }
    return (n * factorial(n - 1));
=======
const lang = 'C is fun';
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  const x = Number(process.argv[2]);
  let i = 0;
  while (i < x) {
    console.log(lang);
    i++;
  }
>>>>>>> 3d6be322d756bed26e3f6828b60cde99aee84365
}
    console.log(factorial(Number(process.argv[2])));