# H, W = [int(i) for i in input().split()]
# A = [[0]*W for _ in range(H)]

# for i in range(H):
#   A[i] = [int(j) for j in input().split()]

# print(A)

import sys
sys.setrecursionlimit(10**6)

h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

ans = 0

def dfs(covered, i, j):
    global ans
    if j == w:
        j = 0
        i += 1
    if i == h:
        now = 0
        for ni in range(h):
            for nj in range(w):
                if not covered[ni][nj]:
                    now ^= a[ni][nj]
        ans = max(ans, now)
        return

    if covered[i][j]:
        dfs(covered, i, j + 1)
    else:
        # 覆わない
        dfs(covered, i, j + 1)
        # 横にペア
        if j + 1 < w and not covered[i][j + 1]:
            covered[i][j] = covered[i][j + 1] = True
            dfs(covered, i, j + 1)
            covered[i][j] = covered[i][j + 1] = False
        # 縦にペア
        if i + 1 < h and not covered[i + 1][j]:
            covered[i][j] = covered[i + 1][j] = True
            dfs(covered, i, j + 1)
            covered[i][j] = covered[i + 1][j] = False

dfs([[False] * w for _ in range(h)], 0, 0)
print(ans)
