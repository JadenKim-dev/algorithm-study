from collections import defaultdict

def solution(tickets):
    graph = defaultdict(lambda: defaultdict(int))
    for fr, to in tickets:
        graph[fr][to] += 1

    candidates = []
    def dfs(fr, visited, route):
        for to in graph[fr].keys():
            if visited[(fr, to)] == graph[fr][to]:
                continue
            new_route = route + [to]
            new_visited = visited.copy()
            new_visited[(fr, to)] += 1

            if sum(new_visited.values()) == len(tickets):
                candidates.append(new_route)
                return
            dfs(to, new_visited, new_route)
    dfs('ICN', defaultdict(int), ['ICN'])
    candidates.sort()
    return(candidates[0] if candidates else [])
# ---

from collections import defaultdict

def solution(tickets):
    graph = defaultdict(lambda: defaultdict(int))
    for fr, to in tickets:
        graph[fr][to] += 1

    for fr in graph.keys():
        graph[fr] = dict(sorted(graph[fr].items()))

    route = ['ICN']
    N = len(tickets) + 1
    def dfs(fr):
        if len(route) == N:
            return True
        for to in graph[fr].keys():
            if (graph[fr][to] == 0):
                continue
            graph[fr][to] -= 1
            route.append(to)
            if dfs(to):
                return True
            
            route.pop()
            graph[fr][to] += 1
        return False
                
    dfs('ICN')
    return route

# print(solution([["ICN", "JFK"], ["ICN", "IAD"], ["JFK", "HND"]]))