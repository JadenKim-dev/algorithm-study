def solution(board):
    size = min(len(board), len(board[0]))
    initial = int("1"*len(board[0]), 2)
    board = [int(''.join(map(str, x)), 2) for x in board]
    while size > 0:
        for i in range(len(board) - size + 1):
            result = initial
            for j in range(size):
                result &= board[i + j]
            result = (bin(result) + "")[2:]
            if "1"*size in result:
                return size**2
        size -= 1
    return 0