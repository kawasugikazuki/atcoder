H, W = map(int,input().split())
A = [[] for _ in range(H)]
H_sum = [0]*H
W_sum = [0]*W

for i in range(H):
  A[i] = [int(j) for j in input().split()]
  H_sum[i]=sum(A[i])
  for j in range(W):
    W_sum[j] += A[i][j]

for i in range(H):
  for j in range(W):
    ans = H_sum[i] + W_sum[j] -A[i][j]
    print(ans,end=" ")
  print()
