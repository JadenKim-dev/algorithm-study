from sys import stdin
from collections import deque
from functools import reduce
EMPTY = 0
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

readints = lambda : map(int, stdin.readline().split())
n, q = readints()
board = [list(readints()) for _ in range(2**n)]
levels = list(readints())

def rotate(r, c, length):
    target = [row[c:c+length] for row in board[r:r+length]]
    result = [[EMPTY]*length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            result[j][length-1-i] = target[i][j]
    for i in range(length):
        for j in range(length):
            board[r+i][c+j] = result[i][j]
        
def melt(board):
    to_be_melted = []
    for r in range(0, 2**n):
        for c in range(0, 2**n):
            if board[r][c] == EMPTY:
                continue
            cnt = 0
            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]
                if nr<0 or nr>=2**n or nc<0 or nc>=2**n:
                    continue
                cnt += board[nr][nc] > 0
            if cnt < 3:
                to_be_melted.append((r, c))
    for r, c in to_be_melted:
        board[r][c] -= 1

def get_max_ice_size_of(board):
    visited = [[False]*(2**n) for _ in range(2**n)]
    max_size = 0
    for r in range(2**n):
        for c in range(2**n):
            if visited[r][c] or board[r][c] == EMPTY:
                continue
            q = deque()
            q.append((r, c))
            visited[r][c] = True
            size = 0
            while q:
                r, c = q.popleft()
                size += 1
                for i in range(4):
                    nr, nc = r+dr[i], c+dc[i]
                    if nr<0 or nr>=2**n or nc<0 or nc>=2**n:
                        continue
                    if visited[nr][nc] or board[nr][nc] == EMPTY:
                        continue
                    q.append((nr, nc))
                    visited[nr][nc] = True
            max_size = max(max_size, size)
    return max_size

for level in levels:
    length = 2**level
    for r in range(0, 2**n, length):
        for c in range(0, 2**n, length):
            rotate(r, c, length)
    melt(board)
print(reduce(lambda a,b : a+sum(b), board, 0))
print(get_max_ice_size_of(board))