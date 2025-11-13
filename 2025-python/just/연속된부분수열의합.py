# 투 포인터로 최소 - 최대 위치 찾기
# n - n 에서 시작해서, 최소값 감소시키면서 확인
    # k를 초과하면 최대값 감소시키기
    # k보다 작으면 최소값 감소시키기
# 가장 앞 쪽 인덱스를 찾기 위해, 답을 찾았다고 바로 반환하면 안 됨
  # 최소값이 0에 도달할 때까지 계속 탐색하기

def solution(sequence, k):
    N = len(sequence) - 1
    x1, x2 = N, N
    curr_sum = sequence[N]
    answer = [0, 1e9]
    while x1 >= 0:
        if curr_sum == k:
            if answer[1] - answer[0] > x2 - x1 or (answer[1] - answer[0] == x2 - x1 and answer[0] > x1):
                answer = [x1, x2]
        if curr_sum >= k:
            curr_sum -= sequence[x2]
            x2 -= 1
        if curr_sum <= k:
            x1 -= 1
            curr_sum += sequence[x1]

    return answer
