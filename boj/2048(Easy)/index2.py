from sys import stdin
from collections import deque
from copy import deepcopy

n = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]

def move(line):
    result = [x for x in line if x > 0]
    for i in range(len(result)-1):
        if result[i] == result[i+1]:
            result[i], result[i+1] = result[i]*2, 0
    result = [x for x in result if x > 0]
    return result + [0]*(n-len(result))

def rotate(board):
    result = deepcopy(board)
    for i in range(n):
        for j in range(n):
            result[n-1-j][i] = board[i][j]
    return result

q = deque(); q.append((0, board))
answer = 0
while q:
    cnt, now = q.popleft()
    if cnt == 5:
        answer = max(answer, max([max(line) for line in now]))
        continue
    for i in range(4):
        tmp = [move(line) for line in now]
        q.append((cnt+1, tmp))
        now = rotate(now)
print(answer)