def solution(n):
    one_cnt = bin(n).count('1')
    while True:
        n += 1
        if bin(n).count("1") == one_cnt:
            return n