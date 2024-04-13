def solution(n):
    result = []
    code_dict = {0:"4", 1:"1", 2:"2"}
    minus_num = {0: 3, 1: 1, 2: 2}
    while n > 0:
        result.append(code_dict[n % 3])
        n = (n - minus_num[n % 3]) // 3
    return ''.join(result[::-1])