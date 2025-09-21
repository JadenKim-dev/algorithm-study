from collections import defaultdict
def solution(n, computers):
    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 0 or i == j:
                continue
            graph[i].append(j)
    visited = set()

    def dfs(n):
        for neighbor in graph[n]:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            dfs(neighbor)
    answer = 0
    for i in range(n):
        if i in visited:
            continue
        answer += 1
        dfs(i)
    
    return answer