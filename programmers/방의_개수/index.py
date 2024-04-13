dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

def solution(arrows):
    r, c = 0, 0
    cycle_cnt = 0
    visited_node = set()
    visited_node.add((0, 0))
    visited_route = set()
    for arrow in arrows:
        for _ in range(2):
            nr, nc = r+dr[arrow], c+dc[arrow]
            if (nr, nc) in visited_node and (r, c, nr, nc) not in visited_route:
                cycle_cnt += 1
            visited_route.add((r, c, nr, nc))
            visited_route.add((nr, nc, r, c))
            visited_node.add((nr, nc))
            r, c = nr, nc
    return cycle_cnt