N = int(input())
A = [int(i) for i in input().split()]

A_sum = [0]*N

total = 0

for i in range(N):
  A_sum[i] += A_sum[i-1] + A[i]

for i in range(N):
  total += A[i]*(A_sum[N-1] - A_sum[i])

print(total)