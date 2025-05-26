from bisect import bisect_left

N, M = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

# O(NM)でTLE
# for cost in B:
#   no_eat = 0
#   for i, able_eat in enumerate(A):
#     if cost >= able_eat and no_eat == i:
#       print(i+1)
#       break
#     else:
#       no_eat += 1
#     if no_eat == len(A):
#       print("-1")

for i in range(1,N):
  A[i] = min(A[i-1],A[i])

A_reversed = [-x for x in A]

for b in B:
  idx = bisect_left(A_reversed,-b)
  if idx == N:
    print("-1")
  else:
    print(idx+1)