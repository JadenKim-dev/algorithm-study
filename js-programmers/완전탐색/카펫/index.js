function solution(brown, yellow) {
  const total = brown + yellow;
  for (let height = 3; height <= Math.sqrt(total); height++) {
    if (total % height !== 0) {
      continue;
    }
    const width = total / height;
    if (width * 2 + height * 2 - 4 === brown) {
      return [width, height];
    }
  }
  return [-1, -1];
}

console.log(solution(8, 1));
