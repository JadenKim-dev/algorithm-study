from sys import stdin

board = [[False]*101 for _ in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
def draw(x, y, d, g):
    history, now = [d], [d]
    board[x][y] = True
    for _ in range(g+1):
        for drc in now:
            x += dx[drc]
            y += dy[drc]
            board[x][y] = True
        now = []
        prev_len = len(history)
        for i in range(prev_len-1, -1, -1):
            nd = (history[i]+1) % 4
            now.append(nd)
            history.append(nd)

n = int(stdin.readline())
for _ in range(n):
    y, x, d, g = map(int, stdin.readline().split())
    draw(x, y, d, g)

answer = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
            answer += 1
print(answer)