from sys import stdin
import heapq
INF = int(1e9)
input = stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n)]
for _ in range(m):
    start, dest, dist = map(int, input().split())
    graph[start-1].append((dest-1, dist))

distance = [INF]*n
prev = [-1]*n


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, dest = heapq.heappop(q)
        if distance[dest] < dist:
            continue
        for x, d in graph[dest]:
            cost = dist+d
            if cost < distance[x] or (cost == distance[x] and dest < prev[x]):
                distance[x] = cost
                prev[x] = dest
                heapq.heappush(q, (cost, x))


start, dest = map(int, input().split())
start -= 1; dest -= 1
dijkstra(start)
print(distance[dest])
path, curr = [dest+1], dest
while prev[curr] != start:
    curr = prev[curr]
    path.append(curr+1)
path.append(start+1)
print(len(path))
for x in reversed(path):
    print(x, end=' ')



