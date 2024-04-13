def solution(land):
    for i in range(len(land)-1):
        for j in range(4):
            land[i+1][j] += max([x for e, x in enumerate(land[i]) if e != j])
    return(max(land[-1]))