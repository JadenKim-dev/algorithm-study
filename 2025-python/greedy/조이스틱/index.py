from collections import deque

def solution(name):
    diff_list = [0] * len(name)
    for i in range(len(name)):
        diff = abs(ord(name[i]) - ord('A'))
        diff = min(diff, abs(26 - diff))
        diff_list[i] = diff

    def go_right(n):
        return 0 if n + 1 >= len(name) else n + 1
    def go_left(n):
        return len(name) - 1 if n - 1 < 0 else n - 1
    curr = 0
    curr_diff_list = diff_list[:]
    curr_diff_list[0] = 0
    queue = deque([(0, 0, curr_diff_list)])
    while queue:
        position, move, curr_diff_list = queue.popleft()
        if sum(curr_diff_list) == 0:
            return sum(diff_list) + move
        if move >= len(name):
            continue
        new_diff_list1 = curr_diff_list[:]
        new_diff_list1[go_right(position)] = 0
        queue.append((go_right(position), move + 1, new_diff_list1))
        new_diff_list2 = curr_diff_list[:]
        new_diff_list2[go_left(position)] = 0
        queue.append((go_left(position), move + 1, new_diff_list2))

# ---

from collections import deque

def solution(name):
    diff_list = [0] * len(name)
    for i in range(len(name)):
        diff = abs(ord(name[i]) - ord('A'))
        diff = min(diff, abs(26 - diff))
        diff_list[i] = diff

    min_move = len(name) - 1
    for i in range(len(name) - 1):
        j = i + 1
        while j < len(name) and diff_list[j] == 0:
            j += 1
        left = i
        right = len(name) - j
        min_move = min(min_move, left * 2 + right, left + right * 2)
    return min_move + sum(diff_list)