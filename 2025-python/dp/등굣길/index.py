from collections import deque

def solution(m, n, puddles):
    EMPTY = 0
    PUDDLE = -1
    memo = [[EMPTY] * m for _ in range(n)]
    for x, y in puddles:
        memo[y-1][x-1] = PUDDLE

    MOVE = [(1, 0), (0, 1)]

    queue = deque([(0, 0)])
    memo[0][0] = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in MOVE:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < m and 0 <= ny < n):
                continue
            if memo[ny][nx] == PUDDLE or memo[ny][nx] != EMPTY:
                continue
            left = max(memo[ny][nx-1] if nx-1 >= 0 else 0, 0)
            up = max(memo[ny-1][nx] if ny-1 >= 0 else 0, 0)

            memo[ny][nx] = (left + up) % 1000000007
            queue.append((nx, ny))
    return memo[n-1][m-1]
