N = input()
A = [int(i) for i in input().split()]
count = 0
tag = False
while True:
  for i in range(len(A)):
    if A[i] % 2 ==1:
      tag = True
  if tag:
    break
  count += 1
  A = [i/2 for i in A]
  

print(count)