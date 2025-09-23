from collections import defaultdict

def solution(triangle):
    memo = [[0] * i for i in range(1, len(triangle) + 1)]
    memo[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(i+1):
            left = memo[i-1][j-1] + triangle[i][j] if j-1 >= 0 else -1
            right = memo[i-1][j] + triangle[i][j] if j <= i-1 else -1
            memo[i][j] = max(left, right)
    return max(memo[-1])