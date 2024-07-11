function solution(n, losts, reserves) {
  const reserveSet = new Set(reserves);
  const borrowSet = new Set();
  const dnList = [-1, 1];

  let borrowCnt = 0;
  losts.forEach((lost) => {
    if (reserveSet.has(lost)) {
      borrowSet.add(lost);
      reserveSet.delete(lost);
    }
  });
  losts.sort((a, b) => a - b);
  losts.forEach((lost) => {
    if (borrowSet.has(lost)) {
      return;
    }
    for (const dn of dnList) {
      currIdx = lost + dn;
      if (currIdx < 1 || currIdx > n) continue;
      if (!reserveSet.has(currIdx)) continue;
      borrowSet.add(currIdx);
      reserveSet.delete(currIdx);
      break;
    }
  });
  return n - losts.length + borrowSet.size;
}
