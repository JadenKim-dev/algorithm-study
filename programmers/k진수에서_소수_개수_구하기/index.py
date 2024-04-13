from collections import deque

def solution(n, k):
    data = convert(n, k)
    answer, prev = 0, 0
    for i in range(1, len(data)):
        if data[i] == '0':
            if data[i-1] != '0':
                answer += is_prime(int(data[prev:i]))
            prev = i
    answer += is_prime(int(data[prev:len(data)]))
                
    return answer

def convert(n, k):
    result = deque()
    while n > 0:
        result.appendleft(str(n % k))
        n //= k
    return ''.join(result)

def is_prime(num):
    if num < 2:
        return False
    limit = int(num ** 0.5)
    for i in range(2, limit + 1):
        if num % i == 0:
            return False
    return True