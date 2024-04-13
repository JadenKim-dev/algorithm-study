def solution(line):
    points = []
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            x, y = intersect(line[i], line[j])
            if int(x) != x or int(y) != y:
                continue
            points.append([int(x), int(y)])
    xlist = sorted([x for x, y in points])
    ylist = sorted([y for x, y in points])
    w = xlist[-1] - xlist[0] + 1
    h = ylist[-1] - ylist[0] + 1
    for i in range(len(points)):
        points[i][0] = points[i][0] - xlist[0]
        points[i][1] = points[i][1] - ylist[0]

    answer = [["."]*w for _ in range(h)]
    for x, y in points:
        answer[y][x] = "*"
    return [''.join(line) for line in answer]

def intersect(line1, line2):
    a, b, e = line1
    c, d, f = line2
    if a*d - b*c == 0:
        return 0.1, 0.1
    else:
        return (b*f - e*d)/(a*d - b*c), -(e*c - a*f)/(a*d - b*c)