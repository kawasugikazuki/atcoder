M = int(input())

A=[]

for i in range(11):
  A += [i] * (M%3)
  M //= 3

print(len(A))
print(*A)