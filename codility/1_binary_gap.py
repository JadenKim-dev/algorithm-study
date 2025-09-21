def solution(N):
    answer = 0
    curr_gap = 0
    in_gap = False

    while N > 0:
        rest = N % 2
        N = N // 2
        if rest == 1:
            if not in_gap:
                in_gap = True
                curr_gap = 0
            elif curr_gap > 0:
                answer = max(answer, curr_gap)
                curr_gap = 0
        elif in_gap:
            curr_gap += 1
        else:
            in_gap = False
    return answer

def solution1(N):
    print(list(map(len, bin(N)[2:].strip('0').split('1'))))
    # return max(map(len, bin(N)[2:].strip('0').split('1')), default=0)

solution(1041)