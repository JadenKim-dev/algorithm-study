from collections import defaultdict
import heapq

def solution(genres, plays):
    song_dict = defaultdict(list)
    sum_dict = defaultdict(int)
    for i in range(len(genres)):
        genre, play = genres[i], plays[i]
        heapq.heappush(song_dict[genre], (-play, i))
        sum_dict[genre] += play
        
    sorted_genres = sorted(list(sum_dict.keys()), key=lambda x:-sum_dict[x])
    answer = []
    for genre in sorted_genres:
        _, idx = heapq.heappop(song_dict[genre])
        answer.append(idx)
        if song_dict[genre]:
            _, idx = heapq.heappop(song_dict[genre])
            answer.append(idx)
    return answer