function solution(word) {
  const ORDER = ["A", "E", "I", "O", "U", ""];
  const candidateSet = new Set();

  function append(curr, cnt) {
    if (cnt === 5) {
      candidateSet.add(curr);
      return;
    }
    for (const char of ORDER) {
      append(curr + char, cnt + 1);
    }
  }
  append("", 0);

  const candidateList = Array.from(candidateSet.keys());
  candidateList.sort();
  return candidateList.indexOf(word);
}

console.log(solution("I"));
