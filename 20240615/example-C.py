N, M = map(int, input().split())
S = [input() for _ in range(N)]

s = [0] * N
for i in range(N):
    for j in range(M):
        if S[i][j] == "o":
            s[i] |= 1 << j

ans = N
for mask in range(1 << N):
    o = 0
    for i in range(N):
        if mask >> i & 1:
            o |= s[i]
    if o == (1 << M) - 1:
        ans = min(ans, bin(mask).count("1"))
print(ans)