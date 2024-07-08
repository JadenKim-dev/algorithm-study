function solution(k, dungeons) {
  let answer = 0;
  comb(dungeons, k);
  /**
   *
   * @param {number[]} restDungeons
   * @param {number} pirodo
   */
  function comb(restDungeons, pirodo) {
    if (restDungeons.length === 0) {
      answer = Math.max(answer, dungeons.length);
      return;
    }
    let canGo = false;
    restDungeons.forEach(([minPirodo, costPirodo], idx) => {
      if (minPirodo > pirodo) return;
      canGo = true;
      const newRestDungeons = [...restDungeons];
      newRestDungeons.splice(idx, 1);
      comb(newRestDungeons, pirodo - costPirodo);
    });
    if (!canGo) {
      answer = Math.max(answer, dungeons.length - restDungeons.length);
    }
  }

  return answer;
}
