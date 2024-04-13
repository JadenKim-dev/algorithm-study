from sys import stdin
from collections import deque
from copy import deepcopy

n = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]

def up(board):
    for i in range(n-1):
        for j in range(n):
            if board[i][j] == 0:
                d = 1
                while i+d+1 < n and board[i+d][j] == 0:
                    d += 1
                for k in range(i, n-d):
                    board[k][j] = board[k+d][j]
                for k in range(n-1, n-d-1, -1):
                    board[k][j] = 0
    for i in range(n-1):
        for j in range(n):
            if board[i][j] == board[i+1][j]:
                board[i][j] *= 2
                for k in range(i+1, n-1):
                    board[k][j] = board[k+1][j]
                board[n-1][j] = 0

def down(board):
    for i in range(n-1, 0, -1):
        for j in range(n):
            if board[i][j] == 0:
                d = 1
                while i-d-1 >= 0 and board[i-d][j] == 0:
                    d += 1                
                for k in range(i, d-1, -1):
                    board[k][j] = board[k-d][j]
                for k in range(d):
                    board[k][j] = 0
    for i in range(n-1, 0, -1):
        for j in range(n):
            if board[i][j] == board[i-1][j]:
                board[i][j] *= 2
                for k in range(i-1, 0, -1):
                    board[k][j] = board[k-1][j]
                board[0][j] = 0

def left(board):
    for j in range(n-1):
        for i in range(n):
            if board[i][j] == 0:
                d = 1
                while j+d+1 < n and board[i][j+d] == 0:
                    d += 1
                for k in range(j, n-d):
                    board[i][k] = board[i][k+d]
                for k in range(n-1, n-d-1, -1):
                    board[i][k] = 0
    for j in range(n-1):
        for i in range(n):
            if board[i][j] == board[i][j+1]:
                board[i][j] *= 2
                for k in range(j+1, n-1):
                    board[i][k] = board[i][k+1]
                board[i][n-1] = 0

def right(board):
    for j in range(n-1, 0, -1):
        for i in range(n):
            if board[i][j] == 0:
                d = 1
                while j-d-1 >= 0 and board[i][j-d] == 0:
                    d += 1
                for k in range(j, d-1, -1):
                    board[i][k] = board[i][k-d]
                for k in range(d):
                    board[i][k] = 0
    for j in range(n-1, 0, -1):
        for i in range(n):
            if board[i][j] == board[i][j-1]:
                board[i][j] *= 2
                for k in range(j-1, 0, -1):
                    board[i][k] = board[i][k-1]
                board[i][0] = 0

q = deque()
q.append((0, board))
answer = 0
while q:
    cnt, now = q.popleft()
    if cnt == 5:
        answer = max(answer, max([max(line) for line in now]))
        continue

    tmp = deepcopy(now)
    up(tmp)
    q.append((cnt+1, tmp))

    tmp = deepcopy(now)
    down(tmp)
    q.append((cnt+1, tmp))

    tmp = deepcopy(now)
    left(tmp)
    q.append((cnt+1, tmp))

    tmp = deepcopy(now)  
    right(tmp)
    q.append((cnt+1, tmp))
    
print(answer)