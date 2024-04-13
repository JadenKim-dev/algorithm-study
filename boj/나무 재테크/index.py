from sys import stdin

n, m, k = map(int, stdin.readline().split())
nutrient = [[5]*n for _ in range(n)]
added = [list(map(int, stdin.readline().split())) for _ in range(n)]
trees = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, stdin.readline().split())
    trees[x-1][y-1].append(z)

di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]
for year in range(k):
    for i in range(n):
        for j in range(n):
            survived = True
            for k in range(len(trees[i][j])-1, -1, -1):
            	# Spring
                if trees[i][j][k] <= nutrient[i][j]:
                    nutrient[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
                else:
                    survived = False
                    break
            if not survived:
                for tree in trees[i][j][:k+1]:
                    nutrient[i][j] += tree // 2 # Summer
                trees[i][j] = trees[i][j][k+1:]
            nutrient[i][j] += added[i][j] # Winter
    # Fall
    breed = [[len([t for t in trees[i][j] if t%5 == 0]) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if breed[i][j] > 0:
                for k in range(8):
                    ni, nj = i + di[k], j + dj[k]
                    if 0 <= ni < n and 0 <= nj < n:
                        trees[ni][nj] += [1]*breed[i][j]

print(sum(sum(len(tree) for tree in line) for line in trees))