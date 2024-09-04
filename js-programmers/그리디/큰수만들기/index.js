function solution(people, limit) {
  people.sort((a, b) => a - b);
  let answer = 0;
  while (people.length > 0) {
    const biggest = people.pop();
    if (biggest + people[0] <= limit) {
      people.shift();
    }
    answer += 1;
  }
  return answer;
}

solution([70, 50, 80, 50], 100);
