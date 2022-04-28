from sys import stdin
import heapq

input = stdin.readline
INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dijkstra():
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    min_cost[0][0] = graph[0][0]
    while q:
        cost, x, y = heapq.heappop(q)
        if x == N-1 and y == N-1:
            return
        if min_cost[x][y] < cost:
            continue
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            new_cost = cost+graph[nx][ny]
            if min_cost[nx][ny] <= new_cost:
                continue
            min_cost[nx][ny] = new_cost
            heapq.heappush(q, (new_cost, nx, ny))


problem_idx = 1
answer = ""
while True:
    N = int(input())
    if N == 0 :
        break
    graph = [list(map(int, input().split())) for _ in range(N)]
    min_cost = [[INF]*N for _ in range(N)]
    dijkstra()
    answer += f'Problem {problem_idx}: {min_cost[N-1][N-1]}\n'
    problem_idx += 1

print(answer)