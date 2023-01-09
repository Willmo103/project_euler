const canSum = (target, numbers = []) => {
  let table = Array(target + 1).fill(false);
  table[0] = true;
  for (let i = 0; i <= target; i++)
    //   adding this flag here instead of inside my second loop it cuts time
    if (table[i] === true)
      for (let j = 0; j < numbers.length; j++) {
        let num = numbers[j];
        if (num + i <= table.length) {
          table[i + num] = true;
        }
      }
  return table[target];
};
//  think of what can change
// coded this one before looking at the solution, took some work but looks good and works
// got hung up trying to use for each on numbers array but simple is better in this case or
// in my trying to understand this at least.

console.log(canSum(7, [5, 3, 4]));
console.log(canSum(7, [2, 4]));
console.log(canSum(7, [2, 3]));
console.log(canSum(8, [2, 2, 4]));
console.log(canSum(300, [7, 14]));
