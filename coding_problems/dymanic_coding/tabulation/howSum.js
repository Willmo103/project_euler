// const howSum = (targetSum, numbers) => {
//   let table = Array(targetSum + 1).fill([false, null]);
//   console.log(table);
//   let steps = [];
//   table[0][0] = true;
//   for (let i = 0; i < targetSum; i++) {
//     if (table[i][0] === true) {
//       for (let j = 0; j < numbers.length; j++) {
//         let num = numbers[j];
//         if (num + i <= table.length) {
//           table[i + num][0] = true;
//           table[i + num][1] = num;
//           //   steps.push([num, i]);
//         }
//         if (table[table.length - 1][0] == true) {
//           for (let n = 0; n < table.length; n++) {
//             if (table[n][0] === true) {
//               steps.push(table[n][1]);
//             }
//           }
//           //   return steps;
//         }
//       }
//     }
//   }
//   return steps;
// };

// first attempt without looking at the solution or listening to the example

const howSum = (target, numbers = []) => {
  let table = Array(target + 1).fill(null);
  table[0] = [];
  for (let i = 0; i <= target; i++)
    if (table[i] !== null) {
      for (let num of numbers) {
        if (num + i <= table.length) {
          table[num + i] = [...table[i], num];
        }
      }
    }
  return table[target];
};

console.log(howSum(7, [3, 4, 5]));
console.log(howSum(7, [3, 4, 5, 7]));
console.log(howSum(7, [2, 4]));
console.log(howSum(8, [2, 3, 5]));
console.log(howSum(300, [7, 14]));

// # this one is much cleaner but i still struggle with syntax on some of the new stuff like using
// the spread operator and getting my indexes working the way i wanted them to
// but with following along I think i can get it just solving the serries of problems with increasing
// complexity is sort of frustrating until i look at the solution. I feel like memoization was a much
// easier concept to grasp because I already had lots of time messing with recursion and tabulation is a
// totally new concept
