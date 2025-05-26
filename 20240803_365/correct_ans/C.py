N,M =map(int,input().split())
A =[int(i) for i in input().split()]

if sum(A) <=M:
  print("infinite")
  exit()

def cond(x):
  s = sum(min(x,a)for a in A)
  return s <= M

ok,ng = 0,max(A)
while ok + 1 < ng:
  mi = (ok + ng) // 2
  if cond(mi):
    ok = mi
  else:
    ng = mi

print(ok)


