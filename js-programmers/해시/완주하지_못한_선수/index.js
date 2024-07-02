function solution(participant, completion) {
  const participantCnt = participant.reduce((acc, name) => {
    if (!acc[name]) {
      acc[name] = 0;
    }
    acc[name] += 1;
    return acc;
  }, {});
  completion.forEach((name) => {
    participantCnt[name] -= 1;
    if (participantCnt[name] === 0) {
      delete participantCnt[name];
    }
  });
  return Object.keys(participantCnt)[0];
}

function solution2(participant, completion) {
  const map = new Map();
  participant.forEach((name) => {
    map.set(name, (map.get(name) || 0) + 1);
  });
  completion.forEach((name) => {
    map.set(name, map.get(name) - 1);
    if (map.get(name) === 0) {
      map.delete(name);
    }
  });
  return map.keys().next().value;
}
