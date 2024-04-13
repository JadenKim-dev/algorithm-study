def solution(n, k, cmds):
    cursor = k
    up = [i-1 for i in range(n)]
    down = [i+1 for i in range(n)]
    is_deleted = [False]*n
    delete_q = []

    for cmd in cmds:
        cmd = cmd.split()
        code = cmd[0]

        if code == 'U':
            for _ in range(int(cmd[1])):
                cursor = up[cursor]

        elif code == 'D':
            for _ in range(int(cmd[1])):
                cursor = down[cursor]

        elif code == 'C':
            delete_q.append(cursor)
            is_deleted[cursor] = True
            if down[cursor] < n:
                up[down[cursor]] = up[cursor]
            if up[cursor] >= 0:
                down[up[cursor]] = down[cursor]
            cursor = down[cursor] if down[cursor] < n else up[cursor]

        elif code == 'Z':
            curr = delete_q.pop()
            is_deleted[curr] = False
            if down[curr] < n:
                up[down[curr]] = curr
            if up[curr] >= 0:
                down[up[curr]] = curr
            while down[curr] < n and is_deleted[down[curr]]:
                down[curr] = down[down[curr]]
            while up[curr] >= 0 and is_deleted[up[curr]]:
                up[curr] = up[up[curr]]
    result = []
    for x in is_deleted:
        result.append("X" if x else "O")
    return ''.join(result)