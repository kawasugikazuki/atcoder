N,T,P = [int(i) for i in input().split()]
L = [int (i) for i in input().split()]

# print(N,T,P,L)
sort_L =sorted(L,reverse=True)
tmp=[0]*P
 
for i in range(P):
  tmp[i] = sort_L[i]

day = T - tmp[P-1]
if day > 0:
  print(day)
else:
  print(0)