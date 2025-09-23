# 모든 정점들과 간접적으로라도 연결되었다고 해서, 나의 순위가 결정되었다는 보장은 없다.
# 간접적으로 이겼다 -> 졌다 로 연결된 경우, 해당 선수와 나와의 순위 상하 관계는 알 수 없다.
# 하지만 이겼다 -> 이겼다 또는 졌다 -> 졌다 로 연결된 경우에는 순위가 확정된다.

# results를 순회해서 graph를 완성, 단방향 그래프로 구성
# win_graph와 lose_graph 두 개를 관리
# win_graph, lose_graph 각각에서 한 번씩 탐색해서, 총 합 몇 명까지 탐색이 가능한지를 계산
# 두 탐색 값의 합이 n - 1인 경우 순위를 알 수 있는 것

from collections import defaultdict, deque

def solution(n, results):
    win_graph = defaultdict(list)
    lose_graph = defaultdict(list)
    for a, b in results:
        win_graph[a].append(b)
        lose_graph[b].append(a)

    def bfs(graph, n):
        visited = set([n])
        queue = deque([n])
        while queue:
            x = queue.popleft()
            for nx in graph[x]:
                if nx in visited:
                    continue
                visited.add(nx)
                queue.append(nx)
        return len(visited) - 1
    answer = 0
    for i in range(1, n + 1):
        win_cnt = bfs(win_graph, i)
        lose_cnt = bfs(lose_graph, i)
        if win_cnt + lose_cnt + 1 == n:
            answer += 1
    return answer

# print(solution(5, [[1, 2], [1, 3], [1, 4], [1, 5]]))
# print(solution(5, [[1, 2], [2, 3], [1, 4], [1, 5]]))
# print(solution(5, [[1, 2], [3, 2], [1, 4], [1, 5]]))
# print(solution(5, [[2, 1], [3, 1], [4, 1], [5, 1]]))
# print(solution(5, [[2, 1], [2, 3], [4, 1], [5, 1]]))
# print(solution(5, [[2, 1], [3, 2], [4, 1], [5, 1]]))