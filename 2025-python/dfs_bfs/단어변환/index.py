from collections import deque

def solution(begin, target, words):    
    def is_changable(s1, s2):
        diff_cnt = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_cnt += 1
            if diff_cnt > 1:
                return False
        return True

    visited = set()
    queue = deque([(begin, 0)])
    while queue:
        curr, d = queue.popleft()
        if (curr == target):
            return d
        visited.add(curr)
        for word in words:
            if word in visited:
                continue
            if not is_changable(curr, word):
                continue
            queue.append((word, d+1))

    return 0
