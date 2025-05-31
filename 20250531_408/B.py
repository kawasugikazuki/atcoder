N = int(input())
A = [int(i) for i in input().split()]

already = []
new_array = []

for a in A:
  if not a in already:
    already.append(a)
    new_array.append(a)

ans = sorted(new_array, reverse=False)
print(len(ans))
for s in ans:
  print(s, end=" ")
print()