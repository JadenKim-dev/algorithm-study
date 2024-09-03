function solution(N, number) {
  const d = new Array(9).fill(null).map((_) => new Set());
  for (let i = 1; i <= 8; i++) {
    d[i].add(+`${N}`.repeat(i));
    for (let j = 1; j < i; j++) {
      for (const n1 of d[j]) {
        for (const n2 of d[i - j]) {
          d[i].add(n1 + n2);
          d[i].add(n1 - n2);
          d[i].add(n1 * n2);
          d[i].add(Math.floor(n1 / n2));
        }
      }
    }
    if (d[i].has(number)) {
      return i;
    }
  }
  return -1;
}

console.log(solution(5, 12));
