function solution(progresses, speeds) {
  const takes = [];
  progresses.forEach((progress, idx) => {
    const speed = speeds[idx];
    takes[idx] = Math.ceil((100 - progress) / speed);
  });

  let currTake = 0;
  let currCnt = 0;
  const result = [];
  takes.forEach((take) => {
    if (currTake === 0) {
      currTake = take;
      currCnt = 1;
      return;
    }
    if (take > currTake) {
      result.push(currCnt);
      currTake = take;
      currCnt = 1;
      return;
    }
    currCnt += 1;
  });
  result.push(currCnt);
  return result;
}

console.log(solution([95, 95, 95, 95], [4, 3, 2, 1]));
