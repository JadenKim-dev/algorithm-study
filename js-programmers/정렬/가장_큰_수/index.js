function solution(numbers) {
  numbers
    .sort((a, b) => {
      const aStr = a + "";
      const bStr = b + "";
      return Number.parseInt(aStr + bStr) < Number.parseInt(bStr + aStr)
        ? -1
        : 1;
    })
    .reverse();
  const result = numbers.join("");
  return result.startsWith("0") ? "0" : result;
}

console.log(solution([0, 0, 0]));
