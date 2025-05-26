import itertools

n,k = map(int,input().split())
s = input()

ans = 0
for t in set(itertools.permutations(s)):
  ok = True
  for i in range(n-k+1):
    u = t[i:i+k]
    if u == u[::-1]: ok = False
  if ok: ans += 1
print(ans)