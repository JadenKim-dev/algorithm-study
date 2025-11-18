# 각 셀이 어떤 병합 그룹에 속했는지를 저장하는 groups
    # 그룹 이름은 첫 병합에서 r, c가 더 적은 셀
# 각 그룹이 어떤 값을 가지는지 나타내는 group_values
# 각 그룹 별 어떤 셀들이 속해있는지를 관리하는 group_cells
from collections import defaultdict

def solution(commands):
    groups = [[None] * 50 for _ in range(50)]
    group_cells = defaultdict(list)
    group_values = dict()
    for i in range(50):
        for j in range(50):
            groups[i][j] = (i, j)
            group_cells[(i, j)].append((i, j))
            group_values[(i, j)] = None

    answer = []
    for command in commands:
        cmd, *args = command.split();
        if cmd == 'PRINT':
            r, c = args
            r, c = int(r)-1, int(c)-1
            group = groups[r][c]
            value = group_values[group]
            answer.append(value if value != None else 'EMPTY')
        elif cmd == 'UPDATE':
            if len(args) == 3:
                r, c, value = args
                r, c = int(r) - 1, int(c) - 1
                group = groups[r][c]
                group_values[group] = value
            else:
                value1, value2 = args
                for group in group_values:
                    if group_values[group] == value1:
                        group_values[group] = value2
        elif cmd == 'MERGE':
            r1, c1, r2, c2 = args
            r1, c1, r2, c2 = int(r1) - 1, int(c1) - 1, int(r2) - 1, int(c2) - 1
            group1, group2 = groups[r1][c1], groups[r2][c2]
            if group1 == group2:
                continue
            for _r, _c in group_cells[group2]:
                group_cells[group1].append((_r, _c))
                groups[_r][_c] = group1
            del group_cells[group2]
            if group_values[group1] == None and group_values[group2] != None:
                group_values[group1] = group_values[group2]
            # print(r1, c1, r2, c2, group2, group_values[group2])
            del group_values[group2]
        elif cmd == 'UNMERGE':
            r, c = args
            r, c = int(r) - 1, int(c) - 1
            group = groups[r][c]
            value = group_values[group]
            for _r, _c in group_cells[group]:
                groups[_r][_c] = (_r, _c)
                group_cells[(_r, _c)] = [(_r, _c)]
                group_values[(_r, _c)] = None
            group_values[(r, c)] = value

    return answer





















