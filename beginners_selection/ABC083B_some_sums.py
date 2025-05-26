N,A,B = [int(i) for i in input().split()]
total = 0
for i in range(N+1):
  keta=str(i)
  sum=0
  for j in keta:
    sum +=int(j)
  if sum >= A and sum <= B:
    total += i 
print(total)