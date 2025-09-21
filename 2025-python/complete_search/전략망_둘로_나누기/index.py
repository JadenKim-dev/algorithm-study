from collections import Counter

def solution(n, wires):
    parent = list(range(n+1))
    def get_parent(n):
        if parent[n] != n:
            parent[n] = get_parent(parent[n])
        return parent[n]
    
    def union(n1, n2):
        u1, u2 = get_parent(n1), get_parent(n2)
        if u1 != u2:
            s1, s2 = sorted([u1, u2])
            parent[s2] = s1 

    wires.sort()

    answer = int(1e9)
    for i in range(len(wires)):
        curr_wires = wires[:i] + wires[(i+1):]
        for v1, v2 in curr_wires:
            union(v1, v2)
        groups = [get_parent(i) for i in range(len(parent))]
        parent_cnt = Counter(groups)
        del parent_cnt[0]
        counts = list(parent_cnt.values())
        diff = abs(counts[0] - counts[1])
        answer = min(diff, answer)

        parent = list(range(n+1))

    return answer

# ---------------------------------------

from collections import defaultdict, deque

def solution(n, wires):
    def bfs(n, graph):
        queue = deque([n])
        visited = set([n])
        
        while queue:
            curr = queue.popleft()
            for v in graph[curr]:
                if v not in visited:
                    visited.add(v)
                    queue.append(v)
        return len(visited)

    answer = int(1e9)
    for i in range(len(wires)):
        rest_wires = wires[:i] + wires[i+1:]
        graph = defaultdict(list)
        for v1, v2 in rest_wires:
            graph[v1].append(v2)
            graph[v2].append(v1)

        cnt1 = bfs(1, graph)
        cnt2 = n - cnt1
        answer = min(abs(cnt1 - cnt2), answer)

    return answer














