from sys import stdin
from collections import deque
from functools import reduce
EMPTY = 0; ROBOT = 1
MAX = int(1e9)

n, k = map(int, stdin.readline().split())
durability = deque(map(int, stdin.readline().split()))
convey = deque([EMPTY]*(2*n))
robots = deque()

def take_down():
    if convey[n-1] == ROBOT:
        robots.popleft()
        convey[n-1] = EMPTY
        
for sec in range(1, MAX):
    durability.rotate(1)
    convey.rotate(1)
    for i in range(len(robots)):
        robots[i] += 1
    take_down()
    
    for i in range(len(robots)):
        dest = robots[i]+1
        if convey[dest] == EMPTY and durability[dest] >= 1:
            robots[i] = dest
            convey[dest] = ROBOT
            convey[dest-1] = EMPTY
            durability[dest] -= 1
    take_down()

    if durability[0] > 0:
        convey[0] = ROBOT
        robots.append(0)
        durability[0] -= 1

    if reduce(lambda a,b: a + (b == 0), durability, 0) >= k:
        print(sec)
        break