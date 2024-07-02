function solution(priorities, location) {
  const sortedPriorites = [...priorities].sort();
  const queue = priorities.map((priority, index) => ({ index, priority }));

  let maxPriority = sortedPriorites.pop();
  let currOrder = 1;
  const runArr = {};
  while (queue.length > 0) {
    const { index, priority } = queue.shift();
    if (priority < maxPriority) {
      queue.push({ index, priority });
      continue;
    }
    runArr[index] = currOrder;
    currOrder += 1;
    maxPriority = sortedPriorites.pop();
  }
  return runArr[location];
}

console.log(solution([2, 1, 3, 2], 2));
