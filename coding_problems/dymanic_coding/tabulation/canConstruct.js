const allConstruct = (target, words) => {
  const table = Array(target.length + 1).fill(false);
  table[0] = true;
  for (let i = 0; i < target.length; i++) {
    if (table[i] === true) {
      for (let word of words) {
        if (target.slice(i, i + word.length) === word) {
          table[i + word.length] = true;
        }
      }
    }
  }
  return table[target.length];
};
console.log(allConstruct("abcdefgh", ["ab", "c", "def", "gh"]));
console.log(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "bo"]));
console.log(
  allConstruct("enterpotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])
);
console.log(
  allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "eee",
    "eeeee",
    "eeee",
    "e",
    "eeeee",
    "eeeeeee",
  ])
);

// got most of the way there on my own before going to the answer and checking my work
