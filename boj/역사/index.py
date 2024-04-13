from sys import stdin
INF = int(1e9)
input = stdin.readline

n, k = map(int, input().split())
graph = [[False]*n for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = True
for t in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = graph[a][b] or (graph[a][t] and graph[t][b])

s = int(input())
for _ in range(s):
    a, b = map(int, input().split())
    if graph[a-1][b-1]:
        print(-1)
    elif graph[b-1][a-1]:
        print(1)
    else:
        print(0)