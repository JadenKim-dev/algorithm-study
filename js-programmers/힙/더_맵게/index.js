function solution(scoville, K) {
  scoville.sort((a, b) => b - a);
  let cnt = 0;
  while (scoville.length >= 2 && scoville[scoville.length - 1] < K) {
    cnt += 1;
    const first = scoville.pop();
    const second = scoville.pop();
    const newScov = first + second * 2;
    console.log({ first, second, newScov });
    scoville.push(newScov);
    scoville.sort((a, b) => b - a);
  }
  if (scoville[scoville.length - 1] < K) {
    return -1;
  }
  return cnt;
}

console.log(solution([1, 1], 5));

console.log(solution([5], 5));
