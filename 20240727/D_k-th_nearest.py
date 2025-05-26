# これだと計算量が大きい
# n,q=[int(i) for i in input().split()]
# a = [int(i) for i in input().split()]
# # b=[0]*q
# # k=[0]*q
# diff=[0]*len(a)

# for i in range(q):
#   b,k= [int(j) for j in input().split()]
#   for l in range(len(a)):
#     diff[l]=abs(b-a[l])
#   s=sorted(diff,reverse=False)
#   print(s[k-1])

# 二分探索する
from bisect import bisect_left, bisect_right

N,Q = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
for _ in range(Q):
  b,k = map(int,input().split())
  lo,hi = -1,10**9
  while lo + 1 < hi:
    mi = (lo+hi) // 2
    c = bisect_right(a,b +mi) - bisect_left(a,b-mi)
    if c >= k:
      hi = mi
    else:
      lo=mi
    print(lo,hi,c)
  print(hi)
