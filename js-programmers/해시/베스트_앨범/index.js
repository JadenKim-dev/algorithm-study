function solution(genres, plays) {
  const playsSum = {};
  const genreToIndexList = {};
  for (let i = 0; i < genres.length; i++) {
    const genre = genres[i];
    const play = plays[i];
    playsSum[genre] = (playsSum[genre] || 0) + play;
    if (!genreToIndexList[genre]) {
      genreToIndexList[genre] = [];
    }
    genreToIndexList[genre].push({ index: i, play });
  }
  const sortedGenres = Object.entries(playsSum)
    .sort((a, b) => b[1] - a[1])
    .map((entry) => entry[0]);
  let result = [];
  for (const genre of sortedGenres) {
    const indexList = genreToIndexList[genre];
    const sortedIndexes = indexList
      .sort((a, b) => {
        const diff = b.play - a.play;
        if (diff !== 0) {
          return diff;
        }
        return a.index - b.index;
      })
      .map(({ index }) => index);
    result = result.concat(sortedIndexes.slice(0, 2));
  }

  return result;
}

console.log(
  solution(
    ["classic", "pop", "classic", "classic", "pop"],
    [500, 600, 150, 800, 2500]
  )
);

console.log(solution(["classic"], [500]));
