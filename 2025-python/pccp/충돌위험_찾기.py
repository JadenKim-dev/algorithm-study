# 전체 상황을 시뮬레이션 할 경우 -> 로봇 하나당 최대 탐색 200 * 최대 경로 길이 100
# -> 전체 순환해도 충분한 시간 복잡도
# 각 경로 route에 대하여, 최소 이동을 수행하는 경로를 bfs를 이용해서 구해서 저장
# route의 최대 길이 만큼 시점을 하나씩 늘려가며, 충돌이 발생하는 횟수를 누적해감

from collections import deque, Counter

def solution(points, routes):
    MAX = 100
    routes = [[p - 1 for p in route] for route in routes]

    def get_min_movement(r, c, tr, tc):
        path = [(r, c)]
        while r != tr:
            r += 1 if r < tr else -1
            path.append((r, c))
        while c != tc:
            c += 1 if c < tc else -1
            path.append((r, c))
        return path

    moves = []
    for route in routes:
        move = []
        for i in range(len(route) - 1):
            fr, to = route[i], route[i+1]
            fr_p, to_p = points[fr], points[to]
            min_move = get_min_movement(fr_p[0], fr_p[1], to_p[0], to_p[1])
            if len(move):
                move.pop()
            move += min_move
        moves.append(move)

    max_time = max(len(move) for move in moves)
    crashes = 0
    for i in range(max_time):
        cnt = Counter(move[i] for move in moves if i < len(move))
        if not len(cnt):
            break
        crashes += sum(v > 1 for v in cnt.values())

    return crashes