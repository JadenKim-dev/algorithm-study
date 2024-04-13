def solution(board):
    answer = 0
    for x in range(0, len(board)):
        for y in range(0, len(board[0])):
            if board[x][y] > 0:
                if x-1 >= 0 and y-1 >= 0:
                    board[x][y] = min(board[x-1][y], board[x][y-1], board[x-1][y-1]) + 1
                answer = max(answer, board[x][y])
    return answer**2