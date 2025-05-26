# 一部うまくいかなかった
N,M = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

left,right = 0,max(A)

# 超える
def is_possible(mid):
  total = 0
  for i in range(N):
    total += min(mid,A[i])
    if total >=M:
      return True
  return False

while left <= right:
  mid = (left + right) // 2
  if is_possible(mid):
    right = mid -1
  else:
    left = mid +1

if left>max(A):
  print("infinite")
else:
  print(left-1)