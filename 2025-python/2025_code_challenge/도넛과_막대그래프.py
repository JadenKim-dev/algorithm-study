# 인입은 되지 않고 나가기만 하는 정점이 추가된 정점인 것으로 보임
  # 다만 막대 그래프에서는 나가기만 하는 정점도 있긴 함
  # 나가기만 하는 애 중 가장 연결된 애가 많은 정점을 고르기
# 간선을 모두 순회하면서 인접 그래프 만들기
# 진입 그래프와 진출 그래프 둘 다 만들어서, 진출은 있는데 진입은 없는 애들을 걸러보기

# 막대 그래프: 진출만 있는 애들에서 시작해서 끝까지 가면서 하나씩 확인
# 도넛 그래프/8자 그래프: 연결된 간선들을 모두 탐색하며 확인

from collections import defaultdict, deque

def solution(edges):
    # 간선을 모두 순회하면서 인접 그래프 만들기, 진입 그래프와 진출 그래프 둘 다
    out_graph = defaultdict(list)
    in_graph = defaultdict(list)
    all_nodes = set()
    
    for fr, to in edges:
        out_graph[fr].append(to)
        in_graph[to].append(fr)
        all_nodes.add(fr)
        all_nodes.add(to)

    # 나가기만 하는 애 중 가장 연결된 애가 많은 정점을 고르기
    candidates = {}
    for n in out_graph.keys():
        if n not in in_graph:
            candidates[n] = len(out_graph[n])

    added_node = max(candidates, key=candidates.get)
    for to in out_graph[added_node]:
        in_graph[to].remove(added_node)
        if not len(in_graph[to]):
            del in_graph[to]
    del out_graph[added_node]
    all_nodes.remove(added_node)
    
    visited = set([added_node])

    def bfs(node):
        queue = deque([node])
        duplicated_cnt = 0
        while queue:
            curr = queue.popleft()
            if not curr in out_graph:
                continue
            for next_node in out_graph[curr]:
                if next_node in visited:
                    duplicated_cnt += 1
                    continue
                visited.add(next_node)
                queue.append(next_node)
        if duplicated_cnt > 1:
            return True
        return False

    bar_cnt = 0
    for n in out_graph.keys():
        if n not in in_graph:
            visited.add(n)
            bfs(n)
            bar_cnt += 1
    eight_cnt = 0
    donut_cnt = 0

    # N = max(out_graph.keys())
    # for n in range(1, N + 1):
    for n in all_nodes:
        if n in visited:
            continue
        visited.add(n)
        is_over_duplicated = bfs(n)
        if n not in out_graph:
            bar_cnt += 1
        elif is_over_duplicated:
            eight_cnt += 1
        else:
            donut_cnt += 1

    return [added_node, donut_cnt, bar_cnt, eight_cnt]
