N,M=[int(i) for i in input().split()]
H=input().split()
index=0
i=0

while M>0:
  M-=int(H[index])
  if M<0:
    break
  index+=1
  if index>=N:
    break

print(index)