function solution(arr) {
  const result = [];

  arr.forEach((num) => {
    if (result[result.length - 1] === num) return;
    result.push(num);
  });
  return result;
}

function solution(arr) {
  return arr.filter((num, idx) => num != arr[idx + 1]);
}

console.log(solution([1, 1, 3, 3, 0, 1, 1]));
