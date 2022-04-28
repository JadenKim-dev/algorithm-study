from sys import stdin
import heapq

input = stdin.readline
INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dijkstra():
    q = []
    heapq.heappush(q, (0, 0, board[0][0]))
    while q:
        x, y, cost = heapq.heappop(q)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            if min_cost[nx][ny] < cost+board[nx][ny]:
                continue
            min_cost[nx][ny] = cost + board[nx][ny]
            heapq.heappush(q, (nx, ny, cost+board[nx][ny]))


N = int(input())
problem_idx = 1
while N != 0:
    board = [list(map(int, input().split())) for _ in range(N)]
    min_cost = [[INF]*N for _ in range(N)]
    dijkstra()
    print("Problem ", problem_idx, ": ", min_cost[N-1][N-1])
    problem_idx += 1
    N = int(input())