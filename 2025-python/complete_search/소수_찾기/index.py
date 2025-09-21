from itertools import permutations

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    visited = set()
    answer = 0
    for i in range(1, len(numbers)+1):
        for p in permutations(numbers, i):
            num = int(''.join(p))
            if num in visited:
                continue
            visited.add(num)
            if is_prime(num):
                answer += 1
    return answer