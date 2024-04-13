from sys import stdin
from collections import deque
from itertools import product
from copy import deepcopy
BLANK = 0

readline = lambda : map(int, stdin.readline().split())
n, m, t = readline()
circles = [deque(list(readline())) for _ in range(n)]

dc, dx = [0, 1], [1, 0]
limit = [n, m]

def sol():
    global circles
    for _ in range(t):
        x, d, k = readline()
        rotate_circles(x, d, k)
        is_deleted, circles = delete_adjacent(circles)
        if not is_deleted:
            change_values(circles)
    return get_total_sum(circles)

def rotate_circles(x, d, k):
    for c_idx in range(x-1, n, x):
        circles[c_idx].rotate(k if d == 0 else -k)

def delete_adjacent(prev_circles):
    def delete_in_circle(c, x):
        is_deleted = False
        for i in range(1, m):
            nx = (x + i) % m
            if prev_circles[c][nx] != prev_circles[c][x]:
                break
            tmp_circles[c][nx] = BLANK
            is_deleted = True
        return is_deleted

    def delete_btw_circles(c, x):
        is_deleted = False
        for nc in range(c+1, n):
            if prev_circles[nc][x] != prev_circles[c][x]:
                break
            tmp_circles[nc][x] = BLANK
            is_deleted = True
        return is_deleted
            
    tmp_circles = deepcopy(prev_circles)
    is_deleted_total = False
    for c in range(n):
        for x in range(m):
            if prev_circles[c][x] == BLANK:
                continue
            is_deleted = False
            is_deleted += delete_in_circle(c, x)
            is_deleted += delete_btw_circles(c, x)
            if is_deleted:
                tmp_circles[c][x] = BLANK
                is_deleted_total = True
    return is_deleted_total, tmp_circles

def change_values(circles):
    not_blank_idxs = [(i, j) for i, j in product(range(n), range(m)) if circles[i][j] != BLANK]
    avg = get_avg(circles, not_blank_idxs)
    for i, j in not_blank_idxs:
        circles[i][j] = circles[i][j]+1 if circles[i][j] < avg \
            else circles[i][j]-1 if circles[i][j] > avg else circles[i][j]

def get_avg(circles, idxs):
    total_sum = 0
    for i, j in idxs:
        total_sum += circles[i][j]
    return total_sum / len(idxs) if len(idxs) > 0 else 0

def get_total_sum(circles):
    return sum([sum(circle) for circle in circles])

print(sol())