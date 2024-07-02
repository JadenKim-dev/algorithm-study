function solution(input) {
  const stack = [];
  for (let i = 0; i < input.length; i++) {
    const currChar = input.charAt(i);
    if (stack.length === 0) {
      if (currChar === ")") {
        return false;
      }
      stack.push(currChar);
      continue;
    }
    if (stack[stack.length - 1] === currChar) {
      stack.push(input.charAt(i));
      continue;
    }
    stack.pop();
  }

  return stack.length === 0;
}

function solution(input) {
  const stack = [];
  for (const currChar of input) {
    if (stack.length === 0) {
      if (currChar === ")") {
        return false;
      }
      stack.push(currChar);
      continue;
    }
    if (stack[stack.length - 1] === currChar) {
      stack.push(currChar);
      continue;
    }
    stack.pop();
  }

  return stack.length === 0;
}
