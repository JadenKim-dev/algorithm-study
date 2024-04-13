from collections import defaultdict, deque
from copy import deepcopy
INF = int(1e9)

def solution(begin, target, words):
    words.append(begin)
    adj_words = defaultdict(list)
    for word1 in words:
        for word2 in words:
            if word1 == word2:
                continue
            diff_cnt = 0
            for c1, c2 in zip(word1, word2):
                diff_cnt += (c1 != c2)
                if diff_cnt > 1:
                    break
            if diff_cnt == 1:
                adj_words[word1].append(word2)
    
    visited = {word:False for word in words}
    q = deque([(begin, 0)])
    while q:
        curr_word, cnt = q.popleft()
        if curr_word == target:
            return cnt
        
        for word in adj_words[curr_word]:
            if visited[word]:
                continue
            visited[word] = True
            q.append((word, cnt+1))
                        
    return 0