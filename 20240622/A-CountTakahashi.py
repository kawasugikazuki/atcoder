N = int(input())
s=[""]*N
count=0
for i in range(N):
  s[i]=input()
  if (s[i] == "Takahashi"):
    count+=1

print(count)
