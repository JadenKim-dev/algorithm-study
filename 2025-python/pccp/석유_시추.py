# 각 좌표에서 bfs를 수행해서 인접한 부분에 탐색 시작 지점 할당
# 탐색 완료 후 전체 석유 크기 계산 후, [시작점]: [시추 양] 형태로 딕셔너리 관리 
# 각각의 가로 좌표에서 시추할 수 있는 석유 양을 합계, 가장 많이 시추할 수 있는 양 구하기

from collections import deque

def solution(land):
    W, H = len(land[0]), len(land)
    
    ground = [[None] * W for _ in range(H)]

    oil_mount = {}
    DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def bfs(h, w):
        ground[h][w] = (h, w)
        visited = set([(h, w)])
        queue = deque([(h, w)])
        while queue:
            ch, cw = queue.popleft()
            for dh, dw in DIR:
                nh, nw = ch + dh, cw + dw
                if not (0 <= nh < H and 0 <= nw < W):
                    continue
                if (nh, nw) in visited or not land[nh][nw]:
                    continue
                ground[nh][nw] = (h, w)
                visited.add((nh, nw))
                queue.append((nh, nw))
            oil_mount[(h, w)] = len(visited)

    for h in range(H):
        for w in range(W):
            if ground[h][w] or land[h][w] == 0:
                continue
            bfs(h, w)

    answer = -1
    for w in range(W):
        visited_oil = set()
        for h in range(H):
            if ground[h][w]:
                visited_oil.add((ground[h][w]))
        answer = max(answer, sum(oil_mount[p] for p in visited_oil))

    return answer
