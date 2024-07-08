function solution(answers) {
  const scores = [0, 0, 0];

  const array1 = [1, 2, 3, 4, 5];
  const array2 = [2, 1, 2, 3, 2, 4, 2, 5];
  const array3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

  answers.forEach((answer, idx) => {
    scores[0] += answer === array1[idx % 5] ? 1 : 0;
    scores[1] += answer === array2[idx % 8] ? 1 : 0;
    scores[2] += answer === array3[idx % 10] ? 1 : 0;
  });

  console.log(scores);
  const maxScore = Math.max(...scores);
  return scores
    .map((score, idx) => (score === maxScore ? idx + 1 : undefined))
    .filter(Boolean);
}
