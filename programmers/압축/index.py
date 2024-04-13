def solution(msg):
    d = {chr(ord('A')+i):i+1 for i in range(26)}
    last, idx, answer = 27, 0, []
    while idx < len(msg):
        size = 2
        while idx+size < len(msg)+1 and msg[idx : idx+size] in d:
            size += 1
        word = msg[idx:idx+size]
        if word not in d:
            d[word] = last
            last += 1
        answer.append(d[msg[idx:idx+size-1]])
        idx += size - 1
    return answer