from itertools import product

def solution(word):
    words = []
    for i in range(1, 6):
        words += [''.join(p) for p in product('AEIOU', repeat=i)]
    words.sort()

    return words.index(word) + 1