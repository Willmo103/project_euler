const bestSum = (targetSum, numbers) => {
  const table = Array(targetSum + 1).fill(null);
  table[0] = [];
  for (let i = 0; i <= targetSum; i++) {
    if (table[i] !== null) {
      for (let num of numbers) {
        let combination = [...table[i], num];
        if (!table[i + num] || table[i + num].length > combination.length) {
          table[i + num] = combination;
        }
      }
    }
  }
  return table[targetSum];
};

console.log(bestSum(7, [2, 5, 3, 4]));
console.log(bestSum(7, [2, 4]));
console.log(bestSum(8, [1, 5, 4]));
console.log(bestSum(100, [2, 5, 1, 25]));

// must be getting tired of staring at computer screen. wrote whole algo but
// got stuck on fetching length of undefined items in the end of the array
// but when i got frustrated and played the video the !table[...] or filter really
// made me smack my head.
