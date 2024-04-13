from sys import stdin
from collections import deque
from functools import reduce
BLANK = 0; BLOCK = 1

n = int(stdin.readline())
blocks = [list(map(int, stdin.readline().split())) for _ in range(n)]

blue = [deque() for _ in range(4)]
green = [deque() for _ in range(4)]

def delete_line_if_full(board, idx):
    global score
    if reduce(lambda a,b : a and len(b)>=idx+1, board, True):
        if reduce(lambda a,b : a and b[idx] == BLOCK, board, True):
            score += 1
            for line in board:
                del line[idx]

def delete_innermost_line(board, num):
    for _ in range(num):
        for line in board:
            if line: line.popleft()

def clear_board(board):
    for line in board:
        for i in range(len(line)-1, -1, -1):
            if line[i] == BLOCK:
                break
            line.pop()
score = 0
for i in range(n):
    type, x, y = blocks[i]
    if type == 1:
        blue[x].append(BLOCK)
        green[y].append(BLOCK)
        
        delete_line_if_full(blue, len(blue[x])-1)
        delete_line_if_full(green, len(green[y])-1)
        
        if len(blue[x]) > 4:
            delete_innermost_line(blue, 1)
        if len(green[y]) > 4:
            delete_innermost_line(green, 1)
        
    elif type == 2:
        blue[x] += [BLOCK, BLOCK]    
        if len(green[y]) < len(green[y+1]):
            len_diff = len(green[y+1]) - len(green[y])
            green[y] += [BLANK]*len_diff
        elif len(green[y]) > len(green[y+1]):
            len_diff = len(green[y]) - len(green[y+1])
            green[y+1] += [BLANK]*len_diff
        green[y].append(BLOCK)
        green[y+1].append(BLOCK)
        
        delete_line_if_full(blue, len(blue[x])-2)
        delete_line_if_full(blue, len(blue[x])-1)
        delete_line_if_full(green, len(green[y])-1)
        
        if len(blue[x]) > 4:
            delete_innermost_line(blue, len(blue[x])-4)
        if len(green[y]) > 4 or len(green[y+1]) > 4:
            delete_innermost_line(green, 1)

    elif type == 3:
        green[y] += [BLOCK, BLOCK]
        if len(blue[x]) < len(blue[x+1]):
            len_diff = len(blue[x+1]) - len(blue[x])
            blue[x] += [BLANK]*len_diff
        elif len(blue[x]) > len(blue[x+1]):
            len_diff = len(blue[x]) - len(blue[x+1])
            blue[x+1] += [BLANK]*len_diff
        blue[x].append(BLOCK)
        blue[x+1].append(BLOCK)
        
        delete_line_if_full(blue, len(blue[x])-1)
        delete_line_if_full(green, len(green[y])-2)
        delete_line_if_full(green, len(green[y])-1)
        
        if len(blue[x]) > 4 or len(blue[x+1]) > 4:
            delete_innermost_line(blue, 1)
        if len(green[y]) > 4:
            delete_innermost_line(green, len(green[y])-4)

    clear_board(blue)
    clear_board(green)

print(score)
get_block_num = lambda board : reduce(lambda a,b: a + sum(b), board, 0)
print(get_block_num(blue) + get_block_num(green))