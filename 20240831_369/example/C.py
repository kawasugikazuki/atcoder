N = int(input())
A = list(map(int, input().split()))
d = [A[i + 1] - A[i] for i in range(N - 1)]
combo, ans = 0, N
for i in range(N - 1):
    if i > 0 and d[i] == d[i - 1]:
        combo += 1
    else:
        combo = 1
    ans += combo
print(ans)
