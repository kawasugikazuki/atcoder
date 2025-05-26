N, K = [ int(i) for i in input().split()]
S = list(input())
count = 0
ans = 0
for i in range(N // K):
  for j, v in enumerate(S):
    if v == 'O':
      count += 1
    else:
      count = 0
    if count == K:
      ans += 1
      for l in range(K):
        S[j-l] = 'X'

print(ans)