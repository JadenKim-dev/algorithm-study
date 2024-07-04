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

function solution(scoville, K) {
  scoville.sort((a, b) => a - b);
  function heapInsert(num) {
    let idx = 0;
    while (true) {
      if (scoville[idx] < num) {
        idx += 1;
      } else {
        console.log({ idx, num });
        scoville.splice(idx, 0, num);
        return;
      }
    }
  }

  let cnt = 0;
  while (scoville.length >= 2 && scoville[0] < K) {
    console.log(scoville);
    cnt += 1;
    const first = scoville.shift();
    const second = scoville.shift();
    const newScov = first + second * 2;
    heapInsert(newScov);
  }
  console.log(scoville);
  if (scoville[0] < K) {
    return -1;
  }
  return cnt;
}

console.log(solution([1, 2, 3, 9, 10, 12], 7));

// console.log(solution([5], 5));
