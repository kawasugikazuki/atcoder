N, K = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

ans =[]*N

for i in range(K, 0,-1):
  ans.append(A[-i])

for i in range(N-K):
  ans.append(A[i])
print(' '.join(map(str, ans)))