N = int(input())

l_array=[]
r_array=[]
for i in range(N):
  A, S = [j for j in input().split()]
  if S == "L":
    l_array.append(int(A))
  else:
    r_array.append(int(A))

l_sum=0
r_sum=0
for i in range(len(l_array)-1):
  l_sum+=abs(l_array[i+1]-l_array[i])

for i in range(len(r_array)-1):
  r_sum+=abs(r_array[i+1]-r_array[i])
print(l_sum+r_sum)

