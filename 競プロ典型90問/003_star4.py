N = int(input())
edge=[[] for _ in range(N)]

for i in range(N-1):
  A, B = [int(j) for j in input().split()]
  a,b = A-1, B-1
  edge[a].append(b)
  edge[b].append(a)

def dfs(s):
  dist = [-1]*N
  dist[s] = 0

  st = [s]
  while st:
    v = st.pop()
    for nv in edge[v]:
      if dist[nv] == -1:
        st.append(nv)
        dist[nv] = dist[v] + 1
  
  return dist

dist0 = dfs(0)
mv = max(enumerate(dist0), key=lambda x: x[1])[0]
distmv = dfs(mv)
print(max(distmv) + 1)