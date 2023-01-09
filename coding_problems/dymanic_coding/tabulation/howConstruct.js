const howConstruct = (target, words) => {
  const table = Array(target.length + 1).fill(0);
  table[0] = 1;
  for (let i = 0; i < target.length; i++) {
    if (table[i] !== 0) {
      for (let word of words) {
        if (target.slice(i, i + word.length) === word) {
          table[i + word.length] += table[i];
        }
      }
    }
  }
  console.log(table);
  return table[target.length];
};

console.log(howConstruct("abcdefgh", ["ab", "c", "def", "gh"]));
console.log(howConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "bo"]));
console.log(howConstruct("purple", ["purp", "p", "ur", "le", "purpl"]));
console.log(
  howConstruct("enterpotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])
);
console.log(
  howConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "eee",
    "eeeee",
    "eeee",
    "e",
    "eeeee",
    "eeeeeee",
  ])
);

// actually wrote the whole working thing without looking!! this one felt more
// fluid now that im starting to understand how this maps out
