def solution(n, t, m, p):
    data = "0"
    for i in range(1, 100000):
        data += convert(i, n)
    return data[p-1::m][:t]

def convert(i, n):  # 10진수 i를 n진법으로
    nums = "0123456789ABCDEF"
    stack = ""
    while i > 0:
        stack += nums[i % n]
        i //= n
    return stack[::-1]
profile
