# 길이가 m인 단어들의 총 개수 -> 26 ** m
# bans를 각 글자 수마다 매핑된 배열로 변환
# 이걸 하나씩 더해가면서, n이 26 ** m - {제외된 개수}  보다 n 이 작거나 같은지 확인
    # 작거나 같다면, n을 26로 나눈 몫과 나머지를 구하고, 이를 기반으로 n 번째 글자를 유추
        # n 앞에 위치한 제외된 주문 개수 만큼 더해줘야 함

from collections import defaultdict

ALPHA = 'abcdefghijklmnopqrstuvwxyz'
ALPHA_MAP = {s: i + 1 for i, s in enumerate(ALPHA)}
N = len(ALPHA)

def convert_to_num(s):
    result = 0
    for i in range(len(s)):
        result += ALPHA_MAP[s[len(s) - i - 1]] * (N ** i)
    return result

def convert_to_str(n):
    result = ''
    while n > 0:
        n -= 1  # 1-based 처리를 위해 먼저 1을 뺌
        result += ALPHA[n % N]
        n = n // N
    return result[::-1]

def solution(n, bans):
    ban_dict = defaultdict(list)
    for b in bans:
        ban_dict[len(b)].append(convert_to_num(b))
    for x in ban_dict:
        ban_dict[x].sort()

    total_words = 0
    total_bans = 0
    for i in range(1, 12):
        total_words += N**i
        if total_words - total_bans - len(ban_dict[i]) < n:
            total_bans += len(ban_dict[i])
            continue

        current_bans = 0
        # ban_dict[i] 에서 n 보다 작은 애들을 모두 선택
        for ban in ban_dict[i]:
            if ban - current_bans - total_bans > n:
                break
            current_bans += 1
        
        num_to_find = n + total_bans + current_bans
        return convert_to_str(num_to_find)
