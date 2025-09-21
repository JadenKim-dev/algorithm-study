from collections import Counter

def solution(A):
    counter = Counter(A)
    return [num for num, cnt in counter.items() if cnt & 1][0]
