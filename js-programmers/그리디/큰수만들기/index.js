function solution(number, k) {
  const nums = number.split("");
  const stack = [nums.shift()];
  nums.forEach((num) => {
    console.log({ num, k, stack });
    while (stack.length > 0 && stack[stack.length - 1] < num && k > 0) {
      k -= 1;
      stack.pop();
    }
    stack.push(num);
  });
  return (k === 0 ? stack : stack.slice(0, number.length - k)).join("");
}

console.log(solution("4177252841", 4));
