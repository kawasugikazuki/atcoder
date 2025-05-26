N = int(input())
d = [0]*N

for i in range(N):
  d[i]=int(input())

newd = sorted(d,reverse=True)

ans =[newd[0]]
for i in range(N):
  if ans[-1] > newd[i]:
    ans.append(newd[i])


print(len(ans))