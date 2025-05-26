H, W, N = [int(i) for i in input().split()]


x_indices = [[] for _ in range(H+1)]
y_indices = [[] for _ in range(W+1)]

ux = [False]*(H+1)
uy = [False]*(W+1)
used = [False]*N

for i in range(N):
  x, y = [int(i) for i in input().split()]
  x_indices[x].append(i)
  y_indices[y].append(i)

Q = int(input())

for _ in range(Q):
  t, v = [int(i) for i in input().split()]
  if t == 1:
    if ux[v]:
      print(0)
    else:
      count = 0
      for i in x_indices[v]:
        if not used[i]:
          used[i] = True
          count += 1
      ux[v] = True
      print(count)
  else:
    if uy[v]:
      print(0)
    else:
      count = 0
      for i in y_indices[v]:
        if not used[i]:
          used[i] = True
          count += 1
      uy[v] = True
      print(count)
