function solution(name) {
  const strMap = new Map(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("").map((alpha, idx) => [alpha, idx])
  );

  let result = 0;
  name.split("").forEach((char) => {
    const alphaDistance = Math.min(
      strMap.get(char),
      strMap.size - strMap.get(char)
    );
    result += alphaDistance;
  });

  let minDistance = name.length - 1;
  for (let i = 1; i < name.length; i++) {
    if (name[i] !== "A") {
      continue;
    }
    for (var j = i + 1; j < name.length; j++) {
      if (name[j] !== "A") {
        break;
      }
    }
    const left = i - 1;
    const right = name.length - j;
    minDistance = Math.min(minDistance, left + 2 * right, left * 2 + right);
    i = j;
  }

  return result + minDistance;
}

console.log(solution("AAAAAAAAABBBBB"));
