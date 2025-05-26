N=input()
bitmask=0
for i in range(len(N)):
  if N[i]=="o":
    bitmask |=  1<<i

print(bitmask)