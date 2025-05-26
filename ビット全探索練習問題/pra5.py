N,M=[int(i) for i in input().split()]
s=[""]*M
bitmask=[0]*N
for i in range(N):
  s[i]=input()

for i in range(N):
  for j in range(M):
    if s[i][j]=="o":
      bitmask[i] |= 1<<j

# print(bitmask)
ans=N
for mask in range(2**N):
  o=0
  for i in range(N):
    if mask >> i & 1:
      o |= bitmask[i]
  if o == (1<<M)-1:
    ans = min(ans,bin(mask).count("1"))

print(ans)