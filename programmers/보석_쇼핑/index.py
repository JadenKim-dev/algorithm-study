def solution(gems):
    n = len(set(gems))
    min_left, min_right, min_len = -1, -1, INF
    left = 0
    for left in range(len(gems)-n+1):
        curr_gems = set()
        for right in range(left, len(gems)):
            if right-left+1 >= min_len:
                break
            curr_gems.add(gems[right])
            if len(curr_gems) == n:
                min_left, min_right, min_len = left, right, right-left+1
    return [min_left+1, min_right+1]