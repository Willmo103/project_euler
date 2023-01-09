const allConstruct = (target, words) => {
  const table = Array(target.length + 1)
    .fill()
    .map(() => []);
  table[0] = [[]];
  for (let i = 0; i < target.length; i++) {
    if (table[i].length >= 0) {
      for (let word of words) {
        if (target.slice(i, i + word.length) === word) {
          const combinations = table[i].map((sub) => [...sub, word]);
          table[i + word.length].push(...combinations);
        }
      }
    }
  }
  //   console.log(table);
  return table[target.length];
};

console.log(allConstruct("abcdefgh", ["ab", "c", "def", "gh"]));
console.log(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "bo"]));
console.log(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]));
console.log(
  allConstruct("enterpotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])
);
// console.log(
//   allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeef", [
//     "eee",
//     "eeeee",
//     "eeee",
//     "e",
//     "eeeee",
//     "eeeeeee",
//   ])
// );

// was able to get to a working solution on this one before going to video but made silly
//  mistake of not mapping out all arrays so duplicated the answers once i saw how it was
//  done i had another head slap moment
