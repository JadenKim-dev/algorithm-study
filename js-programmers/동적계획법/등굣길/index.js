function solution(m, n, puddles) {
  const d = Array.from(Array(n), (_) => Array(m).fill(0));
  for (const [x, y] of puddles) {
    d[y - 1][x - 1] = -1;
  }
  d[0][0] = 1;
  for (let r = 0; r < n; r++) {
    for (let c = 0; c < m; c++) {
      if (d[r][c] === -1) continue;
      if (r + 1 < n && d[r + 1][c] !== -1) {
        d[r + 1][c] = (d[r + 1][c] + d[r][c]) % 1000000007;
      }
      if (c + 1 < m && d[r][c + 1] !== -1) {
        d[r][c + 1] = (d[r][c + 1] + d[r][c]) % 1000000007;
      }
    }
  }

  return d[n - 1][m - 1];
}
