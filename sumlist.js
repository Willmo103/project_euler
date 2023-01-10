const sumList = (head) => {
  let sum = 0;
  let current = head;
  while (current !== null) {
    sum += current.val;
    current = current.next;
  }
  return sum;
};

const sumlistR = (head) => {
  if (head === null) return 0;
  return head.val + sumlistR(head.next);
};
