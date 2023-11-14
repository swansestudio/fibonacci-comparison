const number = 40;

/* Fibonacci recurse */
const fibonacci = function fib(n) {
  return n < 2 ? n : fib(n - 1) + fib(n - 2);
};



/* Fibonacci recurse with cache */
const cache = {};

function fibonacciCached(n) {
  if (cache[n]) {
    return cache[n];
  }
  if (n === 0 || n === 1) {
    return n;
  } else {
    cache[n] = fibonacciCached(n - 1) + fibonacciCached(n - 2);
  }
  return cache[n];
}

/* Driver and time measurement code */
console.time("fibonacci Recurse");
console.log(`Fibonacci of ${number} = ${fibonacci(number)}`);
console.timeEnd("fibonacci Recurse");
console.log();

console.time("fibonacci CACHED");
console.log(`Fibonacci of ${number} = ${fibonacciCached(number)}`);
console.timeEnd("fibonacci CACHED");
console.log();
