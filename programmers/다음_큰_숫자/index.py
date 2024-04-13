def solution(n):
    b = list((bin(n)+"")[2:])
    cnt = [0, 0]; cnt[int(b[len(b)-1])] += 1
    for i in range(len(b)-2, -1, -1):
        if b[i] == "0" and b[i+1] == "1":
            b[i], b[i+1] = b[i+1], b[i]
            return int(''.join(b[:i+1] + sorted(b[i+1:])) , 2)
        cnt[int(b[i])] += 1
    else:
        return int("10" + ''.join(sorted(b[1:])), 2)