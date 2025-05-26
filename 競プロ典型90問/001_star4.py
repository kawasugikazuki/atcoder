N, L = [int(i) for i in input().split()]
K = int(input())
A = [int(i) for i in input().split()]

def check(x):
  num=0
  pre=0
  for i in range(N):
    if A[i] - pre >= x:
      pre = A[i]
      num += 1
  if L - pre >= x:
    num += 1
  
  return num >= K + 1

r, l = L+1, -1

while r - l > 1:
  mid = (r+l)//2
  if check(mid):
    l = mid
  else:
    r = mid

print(l)