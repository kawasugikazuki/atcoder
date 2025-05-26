N,T,A = [int(i) for i in input().split()]


N = N//2
# print(N)

if max(T,A) > N:
  print("Yes")
else:
  print("No")