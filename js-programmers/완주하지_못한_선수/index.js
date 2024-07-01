function solution(participant, completion) {
  const participantSet = new Set(participant);
  completion.forEach((player) => participantSet.delete(player));
  return participantSet.keys().next().value;
}
