from collections import defaultdict

def solution(N, number):
    memo = defaultdict(set)
    for i in range(1, 9):
        memo[i].add(int(str(N) * i))
        for j in range(1, i):
            k = i - j
            for num1 in memo[j]:
                for num2 in memo[k]:
                    memo[i].add(num1 + num2)
                    memo[i].add(num1 - num2)
                    memo[i].add(num1 * num2)
                    if num2 != 0:
                        memo[i].add(num1 // num2)
        if number in memo[i]:
            return i
    return -1
