from sys import stdin
from copy import deepcopy

dices = list(map(int, stdin.readline().split()))
routes = [
    [i for i in range(0, 41, 2)],
    [10, 13, 16, 19, 25, 30, 35, 40],
    [20, 22, 24, 25, 30, 35, 40],
    [30, 28, 27, 26, 25, 30, 35, 40]
    ]

def play(turn, score, prev_pieces, prev_is_goal_in):
    global max_score
    if turn == 10:
        max_score = max(max_score, score)
        return
    for p_idx in range(4):
        if prev_is_goal_in[p_idx]:
            continue
        pieces = deepcopy(prev_pieces)
        is_goal_in = deepcopy(prev_is_goal_in)
        blue, red = pieces[p_idx]
        pieces[p_idx][1] = red = red + dices[turn]
        if red >= len(routes[blue]):
            is_goal_in[p_idx] = True
            play(turn+1, score, pieces, is_goal_in)
        else:
            blue, red = change_route_if_necessary(blue, red)
            pieces[p_idx][0], pieces[p_idx][1] = blue, red
            if not is_already_exists_destination(blue, red, p_idx, pieces, is_goal_in):
                dest_value = routes[blue][red]
                play(turn+1, score+dest_value, pieces, is_goal_in)

def change_route_if_necessary(blue, red):
    if blue == 0 :
        if red == 5: return 1, 0
        elif red == 10: return 2, 0
        elif red == 15: return 3, 0
    return blue, red

def is_already_exists_destination(blue, red, p_idx, pieces, is_goal_in):
    dest_value = routes[blue][red]
    for p_idx2 in range(4):
        if is_goal_in[p_idx2] or p_idx == p_idx2:
            continue
        blue2, red2 = pieces[p_idx2]
        curr_value = routes[blue2][red2]
        if dest_value != curr_value:
            continue

        if dest_value in [16, 22, 24, 26, 28, 30]:
            if blue != blue2 or red != red2 :
                continue
            return True
        else:
            return True
    return False

max_score = 0
pieces = [[0, 0] for _ in range(4)]
is_goal_in = [False]*4
play(0, 0, pieces, is_goal_in)
print(max_score)