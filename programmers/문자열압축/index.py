def figure(n):
    result = 0
    while n > 0:
        n //= 10
        result += 1
    return result

def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2 + 1):
        length = len(s)
        count = 0
        curr = ""
        for k in range(0, len(s)-i + 1, i):
            if s[k:k+i] == curr:
                count += 1
            elif count > 0:
                length = length - count*i + figure(count+1)
                count = 0
            curr = s[k:k+i]
        if count > 0:
            length = length - count*i + figure(count+1)
        answer = min(answer, length)
    return answer
