function solution(sizes) {
  let result = 1000000;
  let lengths = [];
  sizes.forEach(([w, h]) => {
    lengths.push(w);
    lengths.push(h);
  });

  lengths = Array.from(new Set(lengths).keys());

  for (const width of lengths) {
    for (const height of lengths) {
      let isValid = true;
      for (const [w, h] of sizes) {
        if ((w <= width && h <= height) || (h <= width && w <= height)) {
          continue;
        }
        isValid = false;
        break;
      }
      if (isValid) {
        result = Math.min(result, width * height);
      }
    }
  }
  return result;
}

function solution(sizes) {
  const result = sizes.reduce(
    ([accLarge, accSmall], [w, h]) => [
      Math.max(accLarge, Math.max(w, h)),
      Math.max(accSmall, Math.min(w, h)),
    ],
    [0, 0]
  );
  return result[0] * result[1];
}

console.log(
  solution([
    [60, 50],
    [30, 70],
    [60, 30],
    [80, 40],
  ])
);

console.log(
  solution([
    [20, 10],
    [12, 18],
  ])
);
