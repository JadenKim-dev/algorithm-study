function solution(prices) {
  const stack = [];
  const result = new Array(prices.length).fill(0);
  prices.forEach((price, idx) => {
    while (stack.length > 0 && prices[stack[stack.length - 1]] > price) {
      const topIdx = stack.pop();
      result[topIdx] = idx - topIdx;
    }
    stack.push(idx);
  });
  while (stack.length > 0) {
    const topIdx = stack.pop();
    result[topIdx] = prices.length - topIdx - 1;
  }
  return result;
}

console.log(solution([1, 2, 3, 2, 3]));

// 스택에 넣고, 제일 위에 있는 수보다 작은게 들어오면 해당 위치의 결과 값을 설정
//
