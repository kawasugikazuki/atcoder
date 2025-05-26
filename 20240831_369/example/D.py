N = int(input())
A = list(map(int, input().split()))
INF = 10**18

dp = [[0, -INF] for _ in range(N + 1)]
for i in range(N):
    for j in range(2):
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        dp[i + 1][not j] = max(dp[i + 1][not j], dp[i][j] + A[i] * (j + 1))
print(max(dp[N]))
