from sys import stdin
import heapq

input = stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, cows = map(int, input().split())
    graph[a-1].append((b-1, cows))
    graph[b-1].append((a-1, cows))

dist = [INF]*N
def dijkstra():
    q = []
    heapq.heappush(q, (0, 0))
    while q:
        cost, dest = heapq.heappop(q)
        if dest == N-1:
            return
        if dist[dest] < cost:
            continue
        for x, d in graph[dest]:
            new_cost = cost + d
            if new_cost < dist[x]:
                dist[x] = new_cost
                heapq.heappush(q, (new_cost, x))

dijkstra()
print(dist[N-1])