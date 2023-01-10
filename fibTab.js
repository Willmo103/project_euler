const fibTab = (n) => {
  const table = Array(n + 1).fill(0);
  table[1] = 1;

  for (let i = 0; i <= n; i++) {
    table[i + 1] += table[i];
    table[i + 2] += table[i];
  }
  return table[n];
};

// console.log(fibTab(5));
// console.log(fibTab(15));
// console.log(fibTab(50));
// console.log(fibTab(500));

// seem to be able to do this simple problem with tablature without too many issues

const canSum = (target, numbers = []) => {
  let table = Array(target + 1).fill(false);
  table[0] = true;
  for (let i = 0; i <= target; i++) {
    if (table[i] === true) {
      for (let j = 0; j <= numbers.length; j++) {
        let num = numbers[j];
        if (num + i <= table.length) {
          table[i + num] = true;
        }
      }
    }
  }
  //   console.log(table);
  return table[target];
};

// console.log(canSum(7, [3, 4, 5]));

// in attempting this problem again I was able to get all the logic correct
// but the in my i loop I set my stop at the table.length and got a weird error
// in comparing it to the code i wrote last night i realized that the target was
// the best choice to iterate through as the table length will potentially become
// longer and longer pre JS weird array logic under the hood.

const howSum = (target, numbers) => {
  const table = Array(target + 1).fill(null);
  table[0] = [];
  for (i = 0; i < target; i++) {
    if (table[i] !== null) {
      for (let num of numbers) {
        // gotta look up the in vs of for these loops
        if (table[i + num] <= table.length) {
          table[i + num] = [...table[i], num];
        }
      }
    }
  }
  return table[target];
};

// console.log(howSum(7, [3, 4, 5]));

// coded this okay, needed to make one change from (nums in numbers) to (num of numbers)

const bestSum = (target, numbers) => {
  const table = Array(target + 1).fill(null);
  table[0] = [];
  for (let i = 0; i < target; i++) {
    if (table[i] !== null) {
      for (let num of numbers) {
        let combination = [...table[i], num];
        if (!table[i + num] || table[i + num].length > combination.length) {
          table[i + num] = combination;
        }
      }
    }
  }
  return table[target];
};

// console.log(bestSum(7, [3, 4, 5]));
// console.log(bestSum(7, [2, 2, 5]));
// console.log(bestSum(300, [2, 2, 5]));

// again logic is okay with me but the syntax tends to hold me up
// in this case it was missing adding .length in my comparison of table[i+num].length > combination
// i missed adding .length to the combination variable
