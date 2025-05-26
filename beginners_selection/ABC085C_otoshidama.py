N,Y = [int(i) for i in input().split()]
tag=False
for i in range(N+1):
  for j in range(N-i+1):
    k = N-i-j
    # print(i,j,k)
    total = 10000*i+5000*j+1000*k
    if total == Y:
      tag=True
      ans =[i,j,k]

if tag:
  print(ans[0],ans[1],ans[2])
else:
  print(-1,-1,-1) 