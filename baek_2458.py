from sys import stdin

input = stdin.readline
SMALL = -1; LARGE = 1; UNKNOWN = 0; SELF = 2

N, M = map(int, input().split())
dist = [[False]*N for _ in range(N)]

for i in range(N):
    dist[i][i] = SELF

for _ in range(M):
    a, b = map(int, input().split())
    dist[a-1][b-1] = SMALL
    dist[b-1][a-1] = LARGE

for k in range(N):
    for a in range(N):
        for b in range(N):
            if dist[a][b] != UNKNOWN:
                continue
            if dist[a][k] != UNKNOWN and dist[a][k] == dist[k][b]:
                dist[a][b] = dist[a][k]

cnt = 0
for i in range(N):
    for j in range(N):
        is_all_known = True
        if dist[i][j] == UNKNOWN:
            is_all_known = False
            break
    cnt += is_all_known
print(cnt)