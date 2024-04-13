from copy import deepcopy
max_diff, max_board = 0, []
def solution(n, info):
    def dfs(ascore, lscore, cnt, idx, board):
        global max_diff, max_board
        if cnt > n:
            return
        if idx > 10:
            diff = lscore - ascore
            if diff > max_diff:
                board[10] = n - cnt
                max_board = board
                max_diff = diff
            return
        if cnt < n:
            board2 = deepcopy(board); board2[10-idx] = info[10-idx] + 1
            dfs(ascore, lscore+idx, cnt+info[10-idx]+1, idx+1, board2)
            
        board1 = deepcopy(board)
        
        if info[10-idx] > 0:
            dfs(ascore+idx, lscore, cnt, idx+1, board1)            
        else:
            dfs(ascore, lscore, cnt, idx+1, board1)
            
    dfs(0, 0, 0, 0, [0]*11)
    return max_board if max_board else [-1]