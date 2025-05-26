N = int(input())
K = [int(i) for i in input().split()]
ans = sum(K)

for bit in range(1 << N):
  a = 0
  b = 0
  for i in range(N):
    if bit >> i & 1:
      a += K[i]
    else:
      b += K[i]
  ans = min(ans, max(a, b))

print(ans)