N = 12
count = 0

for i in range(N):
  moji = input()
  if len(moji) == i+1:
    count +=1

print(count)