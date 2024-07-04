function solution(operations) {
  const queue = [];

  operations.forEach((operation) => {
    console.log(queue);
    const [operator, operand] = operation.split(" ");
    if (operator === "I") {
      queue.push(Number.parseInt(operand));
      return;
    }
    if (queue.length === 0) {
      return;
    }
    queue.sort((a, b) => a - b);
    if (operand === "1") {
      queue.pop();
    } else {
      queue.shift();
    }
  });

  queue.sort((a, b) => a - b);
  return queue.length === 0 ? [0, 0] : [queue[queue.length - 1], queue[0]];
}

console.log(
  solution([
    "I -45",
    "I 653",
    "D 1",
    "I -642",
    "I 45",
    "I 97",
    "D 1",
    "D -1",
    "I 333",
  ])
);
