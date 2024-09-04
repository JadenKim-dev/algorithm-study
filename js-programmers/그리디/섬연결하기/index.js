function findParent(parent, x) {
  if (parent[x] != x) {
    parent[x] = findParent(parent, parent[x]);
  }
  return parent[x];
}

function unionParent(parent, a, b) {
  const parentA = findParent(parent, a);
  const parentB = findParent(parent, b);
  if (parentA < parentB) {
    parent[parentB] = parentA;
  } else {
    parent[parentA] = parentB;
  }
}

function solution(n, costs) {
  costs.sort((a, b) => a[2] - b[2]);
  let answer = 0;
  const parent = Array.from({ length: n }, (_, i) => i);
  for (const [from, to, cost] of costs) {
    if (findParent(parent, from) === findParent(parent, to)) {
      continue;
    }
    unionParent(parent, from, to);
    answer += cost;
  }

  return answer;
}

console.log(
  solution(4, [
    [0, 1, 1],
    [2, 3, 1],
    [1, 2, 4],
  ])
);
