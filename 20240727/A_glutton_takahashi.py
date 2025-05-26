N = int(input())
count=0
s=[""]*N
tag = False
for i in range(N):
  s = input()
  if count ==2:
    tag = True
  if s == "sweet":
    count+=1
  else:
    count=0

if tag:
  print("No")
else:
  print("Yes")