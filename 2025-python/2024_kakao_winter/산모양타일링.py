# 각 열에서 3 ~ 4개의 삼각형을 하나의 단위로 묶어서 생각
    # top == 1
        # 마지막 삼각형 안 먹은 케이스: 3
        # 마지막 삼각형 먹은 케이스: 1
    # top == 0
        # 마지막 삼각형 안 먹은 케이스: 2
        # 마지막 삼각형 먹은 케이스: 1
# 2개로 묶을 경우의 케이스
    # top == 1
        # 마지막 삼각형 안 먹은 케이스: 
            # prev_마지막 삼각형 안 먹은 케이스 * 3
            # + prev_마지막 삼격형 먹은 케이스 * 2
        # 마지막 삼격형 먹은 케이스:
            # prev_마지막 삼각형 안 먹은 케이스 * 1
            # + prev_마지막 삼격형 먹은 케이스 * 1
    # top == 0
         # 마지막 삼각형 안 먹은 케이스: 
            # prev_마지막 삼각형 안 먹은 케이스 * 2
            # + prev_마지막 삼격형 먹은 케이스 * 1
        # 마지막 삼격형 먹은 케이스:
            # prev_마지막 삼각형 안 먹은 케이스 * 1
            # + prev_마지막 삼격형 먹은 케이스 * 1

# dp 관리 시 마지막 삼각형 먹은 케이스 / 안 먹은 케이스로 분리해서 누적해감

def solution(n, tops):
    dp = [(3, 1) if tops[0] == 1 else (2, 1)]
    for i in range(1, n):
        prev_cases = dp[i-1]
        if tops[i] == 1:
            opened = (prev_cases[0] * 3 + prev_cases[1] * 2) % 10007
            closed = (prev_cases[0] + prev_cases[1]) % 10007
            dp.append((opened, closed))
        else:
            opened = (prev_cases[0] * 2 + prev_cases[1] * 1) % 10007
            closed = (prev_cases[0] + prev_cases[1]) % 10007
            dp.append((opened, closed))
    return sum(dp[-1]) % 10007
