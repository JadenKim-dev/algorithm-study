function solution(citations) {
  let currIndex = 0;
  for (let i = 0; i < 10000; i++) {
    const overCnt = citations.filter((c) => c >= i).length;
    if (overCnt >= i) {
      currIndex = Math.max(currIndex, i);
    }
  }
  return currIndex;
}

console.log(solution([10]));
