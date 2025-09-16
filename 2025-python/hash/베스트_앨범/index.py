from collections import defaultdict

def solution(genres, plays):
    genreToPlays = defaultdict(list)
    genreToPlaySum = defaultdict(int)
    for i in range(len(plays)):
        genre = genres[i]
        play = plays[i]
        genreToPlays[genre].append({ "idx": i, "play": play })
        genreToPlaySum[genre] += play
    answer = []
    for genre, _ in sorted(genreToPlaySum.items(), key=lambda x:-x[1]):
        playsInGenre = genreToPlays[genre]
        playsInGenre.sort(key=lambda x: (-x["play"], x["idx"]))
        answer.extend([obj["idx"] for obj in playsInGenre[:2]])
        
    return answer