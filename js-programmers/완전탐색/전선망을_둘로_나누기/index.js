function solution(n, wires) {
  let visitedList = new Array(n + 1).fill(false);
  let graph = Array.from({ length: n + 1 }, () => []);
  function dfs(curr) {
    if (!visitedList[curr]) {
      visitedList[curr] = true;
      for (const e of graph[curr]) {
        dfs(e);
      }
    }
  }

  let answer = n + 1;
  for (let i = 0; i < wires.length; i++) {
    const currWires = [...wires];
    currWires.splice(i, 1);

    currWires.forEach(([e1, e2]) => {
      graph[e1].push(e2);
      graph[e2].push(e1);
    });
    dfs(1);

    const size1 = visitedList
      .slice(1)
      .reduce((acc, visited) => (visited ? acc + 1 : acc), 0);
    const size2 = n - size1;
    answer = Math.min(answer, Math.abs(size1 - size2));

    visitedList = new Array(n + 1).fill(false);
    graph = Array.from({ length: n + 1 }, () => []);
  }
  return answer;
}

console.log(
  solution(9, [
    [1, 3],
    [2, 3],
    [3, 4],
    [4, 5],
    [4, 6],
    [4, 7],
    [7, 8],
    [7, 9],
  ])
);

// 1
// 2
// 3
// 4 2
// 5 2
// 6 3
// 7 3
// 8
// 9 2
// 10 2
// 11 3
// 12 3
