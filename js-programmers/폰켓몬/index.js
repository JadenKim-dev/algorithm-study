// https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=javascript

function solution(nums) {
  const numCnt = nums.reduce((acc, num) => {
    if (!acc[num]) acc[num] = 0;
    acc[num] += 1;
    return acc;
  }, {});
  const numCntEntries = Object.entries(numCnt);
  const take = nums.length / 2;
  if (take > numCntEntries.length) {
    return numCntEntries.length;
  }
  return take;
}

function solution2(nums) {
  const numSet = new Set(nums);
  const take = nums.length / 2;
  return numSet.size < take ? numSet.size : take;
}

console.log(solution([3, 1, 2, 3]));
