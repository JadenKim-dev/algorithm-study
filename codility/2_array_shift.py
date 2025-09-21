def solution(A, K):
    K %= len(A)
    return A[-K:] + A[:-K]

print(solution([1, 2, 3, 4, 5], 8))