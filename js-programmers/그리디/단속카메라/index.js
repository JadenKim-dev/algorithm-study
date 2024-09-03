/**
 *
 * @param {[number, number][]} routes
 * @returns
 */
function solution(routes) {
  routes.sort((a, b) => {
    return a[1] - b[1];
  });

  let count = 0;
  let currCamera = -30001;
  for (const [from, to] of routes) {
    if (currCamera < from) {
      currCamera = to;
      count += 1;
    }
  }
  return count;
}

console.log(
  solution([
    [-20, -15],
    [-14, -5],
    [-18, -13],
    [-20, -18],
    [-5, -3],
  ])
);
