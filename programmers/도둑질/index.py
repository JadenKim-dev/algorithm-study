def solution(money):    
    q = [0]*len(money)
    q[0], q[1] = money[0], max(money[0], money[1])
    for i in range(2, len(money)-1):
        q[i] = max(q[i-1], q[i-2]+money[i])
    
    q2 = [0]*len(money)
    q2[0], q2[1] = 0, money[1]
    for i in range(2, len(money)):
        q2[i] = max(q2[i-1], q2[i-2]+money[i])
    return max(q[-2], q2[-1])