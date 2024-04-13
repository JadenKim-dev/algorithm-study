from sys import stdin
from collections import deque

n, k = [int(stdin.readline()) for _ in range(2)]
board = [[0]*n for _ in range(n)]
for _ in range(k):
    x, y = map(int, stdin.readline().split())
    board[x-1][y-1] = 1
l = int(stdin.readline())
convert = lambda x : [int(x[0]), x[1]]
changes = [convert(stdin.readline().split()) for _ in range(l)]
changes.reverse()

def sol():
    snake = deque()
    x, y, d = 0, 0, 0
    snake.append((x, y))
    board[x][y] = 2
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(1, 10200):
        nx, ny = x + dx[d], y + dy[d]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            return i
        if board[nx][ny] == 2:
            return i
        snake.append((nx, ny))
        if board[nx][ny] == 1:
            board[nx][ny] = 0
        else:
            px, py = snake.popleft()
            board[px][py] = 0
        board[nx][ny] = 2
        x, y = nx, ny

        if changes and i == changes[-1][0]:
            if changes[-1][1] == 'L':
                d = (d - 1) % 4
            elif changes[-1][1] == 'D':
                d = (d + 1) % 4
            changes.pop()
print(sol())
