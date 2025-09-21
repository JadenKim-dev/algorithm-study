def solution(N):
    answer = 0
    curr_gap = 0
    in_gap = False

    while N:
        if N & 1:
            if in_gap:
                answer = max(answer, curr_gap)
            in_gap = True
            curr_gap = 0
        elif in_gap:
            curr_gap += 1
        N >>= 1
    return answer

def solution1(N):
    print(list(map(len, bin(N)[2:].strip('0').split('1'))))
    # return max(map(len, bin(N)[2:].strip('0').split('1')), default=0)

print(solution(1041))