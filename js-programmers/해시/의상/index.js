function solution(clothes) {
  const categoryCnt = {};
  for ([_, category] of clothes) {
    categoryCnt[category] = (categoryCnt[category] || 0) + 1;
  }
  return (
    Object.values(categoryCnt).reduce((acc, cnt) => acc * (cnt + 1), 1) - 1
  );
}
