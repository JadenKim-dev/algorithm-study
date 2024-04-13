from sys import stdin

board = [[False]*101 for _ in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
flows = [[0]]
for _ in range(10):
    flows.append(flows[-1] + [i+1 for i in flows[-1][::-1]])

def draw(x, y, d, g):
    board[x][y] = True
    for f in flows[g]:
        x += dx[(f+d)%4]
        y += dy[(f+d)%4]
        board[x][y] = True

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