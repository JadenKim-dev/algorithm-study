# 모든 간선을 순회하면서 인접 노드에 대한 graph를 완성한다
# bfs로 1번에서 가까운 노드들에서 시작해서, 전체 노드들을 순회한다.
# 각 노드들을 순회할 때에는 노드 별로 거리를 저장하는 딕셔너리에 현재 거리를 기록한다.
# 모든 노드를 순회한 후 가장 먼 노드들의 개수를 집계한다.

from collections import defaultdict, deque

def solution(n, edges):
    graph = defaultdict(list)
    for i in range(len(edges)):
        x, y = edges[i]
        graph[x].append(y)
        graph[y].append(x)
    queue = deque([(1, 0)])
    distance = { 1: 0 }
    
    while queue:
        x, d = queue.popleft()
        for nx in graph[x]:
            if nx in distance:
                continue
            distance[nx] = d + 1
            queue.append((nx, d + 1))
    max_value = max(distance.values())
    return len([val for val in distance.values() if val == max_value])
    
# print(solution(2, [[1, 2]]))
# print(solution(2, [[1, 2], [2, 3]]))
# print(solution(2, [[1, 2], [2, 3], [1, 3]]))