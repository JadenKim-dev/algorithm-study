from collections import defaultdict

def solution(clothes):
    cloth_cnt = defaultdict(int)
    for cloth in clothes:
        cloth_cnt[cloth[1]] += 1
    result = 1
    for cnt in cloth_cnt.values():
        result *= cnt + 1
    return result - 1

# --------------------------------

from collections import Counter
from math import prod

def solution(clothes):
    clothes_cnt = Counter(category for _, category in clothes)
    return prod(c + 1 for c in clothes_cnt.values()) - 1
