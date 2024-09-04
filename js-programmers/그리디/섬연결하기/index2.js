function solution(n, costs) {
  costs.sort((a, b) => a[2] - b[2]);
  const [from, to, cost] = costs.shift();
  const connected = new Set([from, to]);
  let answer = cost;
  while (connected.size < n) {
    const idx = costs.findIndex(
      ([from, to]) =>
        (connected.has(from) && !connected.has(to)) ||
        (!connected.has(from) && connected.has(to))
    );
    const [[from, to, cost]] = costs.splice(idx, 1);
    answer += cost;
    connected.add(from).add(to);
    console.log({ connected });
  }
  return answer;
}

console.log(
  solution(4, [
    [0, 1, 1],
    [0, 2, 2],
    [1, 2, 5],
    [1, 3, 1],
    [2, 3, 8],
  ])
);
