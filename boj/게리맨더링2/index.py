from sys import stdin

n = int(stdin.readline())
people = [[0]*(n+1)] + [[0] + list(map(int, stdin.readline().split())) for _ in range(n)]
def sol():
    min_diff = int(1e9)
    for x in range(1, n+1):
        for y in range(1, n+1):
            for d1 in range(1, n+1):
                for d2 in range(1, n+1):
                    if x+d1+d2 > n: continue
                    if y-d1 < 1: continue
                    if y+d2 > n: continue
                    diff = get_people_diff(x, y, d1, d2)
                    min_diff = min(min_diff, diff)
    return min_diff

def get_people_diff(x, y, d1, d2):
    is_five = [[False]*(n+1) for _ in range(n+1)]
    for i in range(d1+1):
        is_five[x+i][y-i] = True
    for i in range(d2+1):
        is_five[x+i][y+i] = True
    for i in range(d2+1):
        is_five[x+d1+i][y-d1+i] = True
    for i in range(d1+1):
        is_five[x+d2+i][y+d2-i] = True
    
    sums = [0]*6
    for r in range(1, x+d1):
        for c in range(1, y+1):
            if is_five[r][c]:
                break
            sums[1] += people[r][c]

    for r in range(1, x+d2+1):
        for c in range(n, y, -1):
            if is_five[r][c]:
                break
            sums[2] += people[r][c]
    
    for r in range(x+d1, n+1):
        for c in range(1, y-d1+d2):
            if is_five[r][c]:
                break
            sums[3] += people[r][c]
    
    for r in range(x+d2+1, n+1):
        for c in range(n, y-d1+d2-1, -1):
            if is_five[r][c]:
                break
            sums[4] += people[r][c]
    sums[5] = sum([sum(row) for row in people]) - sum(sums[1:5])

    return max(sums)-min(sums[1:])

print(sol())