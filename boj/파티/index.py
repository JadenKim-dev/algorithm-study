from sys import stdin
from collections import deque
INF = int(1e9)
input = stdin.readline

N, M, X = map(int, input().split())
X -= 1
graph = [[] for _ in range(N)]
reverse_graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a-1].append((b-1, c))
    reverse_graph[b-1].append((a-1, c))

def dijstra(graph, X):
    dist_list = [INF]*N
    dist_list[X] = 0
    q = deque([(X, 0)])
    while q:
        x, d = q.popleft()
        if dist_list[x] < d:
            continue
        for xx, dd in graph[x]:
            cost = d + dd
            if cost < dist_list[xx]:
                dist_list[xx] = cost
                q.append((xx, cost))
    return dist_list

to_dist = dijstra(graph, X)
from_dist = dijstra(reverse_graph, X)
print(max([a+b for a, b in zip(to_dist, from_dist)]))