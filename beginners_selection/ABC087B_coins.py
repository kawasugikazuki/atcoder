A_500 = int(input())
B_100 = int(input())
C_50 = int(input())
x = int(input())

count = 0

for i in range(A_500+1):
  for j in range(B_100+1):
    for k in range(C_50+1):
      # print(i,j,k)
      if 500*(i)+100*(j)+50*(k) == x:
        count+=1

print(count)
