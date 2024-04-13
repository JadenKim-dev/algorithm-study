from sys import stdin
from collections import deque

wheels = [deque(list(stdin.readline().strip())) for _ in range(4)]
k = int(stdin.readline())

def rotate(w_num, direction):
    visited[w_num] = True
    if w_num+1 < 4 and not visited[w_num+1] and wheels[w_num][2] != wheels[w_num+1][6]:
        rotate(w_num+1, -direction)
    if w_num-1 >= 0 and not visited[w_num-1] and wheels[w_num][6] != wheels[w_num-1][2]:
        rotate(w_num-1, -direction)
    wheels[w_num].rotate(direction)

for _ in range(k):
    visited = [False] * 4
    w_num, direction = map(int, stdin.readline().split())
    rotate(w_num-1, direction)
    
print(int(wheels[0][0]) + int(wheels[1][0])*2 + int(wheels[2][0])*4 + int(wheels[3][0])*8)