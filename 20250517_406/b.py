N, K = [int(i) for i in input().split()]

A = [int(i) for i in input().split()]

total = 1

for a in A:
  total = total * a
  if total >= 10**K:
    total = 1

print(total)