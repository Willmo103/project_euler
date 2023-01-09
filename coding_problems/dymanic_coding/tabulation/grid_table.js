const grid_traveler = (m, n) => {
  table = Array(m + 1)
    .fill()
    .map(() => Array(n + 1).fill(0));
  table[1][1] = 1;
  for (let i = 0; i <= m; i++) {
    for (let j = 0; j <= n; j++) {
      const current = table[i][j];
      if (j + 1 <= n) table[i][j + 1] += current;
      if (i + 1 <= m) table[i + 1][j] += current;
    }
  }
  return table[m][n];
};

console.log(grid_traveler(1, 1));
console.log(grid_traveler(3, 3));
console.log(grid_traveler(3, 2));
console.log(grid_traveler(7, 3));
console.log(grid_traveler(18, 18));

// tabulation will offer a quick solution right away but visualization will change
// must figure out how to use a table to answer your questions

// visualize the problem as a table
//  size the table based on the inputs
// initialize the table with default values
// seed the trivial answer into the table
//  iterate through the table
// fill further positions based on current positions
