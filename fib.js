const fib = (n) => {
  if (n <= 2) return 1;
  return fib(n - 1) + fib(n - 2);
};

// console.log(fib(7));
// console.log(fib(12));
// console.log(fib(9));
// console.log(fib(50));

const fibMemo = (n, memo = {}) => {
  if (n in memo) return memo[n];
  if (n <= 2) return 1;
  memo[n] = fibMemo(n - 1, memo) + fibMemo(n - 2, memo);
  //   memo[n] = fib(n - 1, memo) + fib(n - 2, memo); // < --- was calling fib() instead of fibMemo()
  return memo[n];
};

console.log(fibMemo(7));
console.log(fibMemo(12));
console.log(fibMemo(9));
console.log(fibMemo(50));

// cannot figure out why all of the sudden this same logic in JS is no longer working
// memo only updates on last call of function and stores no values along the way
// preventing the memo from being useful

// It helps if i call the same function as in fibMemo, instead of fib in my memoized calls... dumb mistake
