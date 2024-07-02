function solution(bridge_length, weight_limit, truck_weights) {
  const queue = [];
  let time = 0;
  let currWeightSum = 0;
  let lastEntered = -1;
  do {
    time += 1;

    queue.forEach((item) => {
      item.time -= 1;
    });

    if (queue[0]?.time === 0) {
      const { index } = queue.shift();
      currWeightSum -= truck_weights[index];
    }

    if (
      currWeightSum + truck_weights[lastEntered + 1] <= weight_limit &&
      queue.length + 1 <= bridge_length
    ) {
      lastEntered += 1;
      currWeightSum += truck_weights[lastEntered];
      queue.push({ time: bridge_length, index: lastEntered });
    }
  } while (queue.length > 0);
  return time;
}

console.log(solution(10000, 1, new Array(10000).fill(1)));
