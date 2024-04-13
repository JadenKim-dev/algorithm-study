def solution(n, wires):
    answer = int(1e9)
    for i in range(len(wires)):
        now = wires[:i] + wires[i+1:]
        parent = [i for i in range(n+1)]
        for a, b in now:
            union_parent(parent, a, b)
        for i in range(1, n+1):
            find_parent(parent, i)
        m1 = len([x for x in parent[1:] if x == parent[1]])
        m2 = len([x for x in parent[1:] if x != parent[1]])
        answer = min(answer, abs(m1-m2))
    return answer

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b