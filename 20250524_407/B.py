X, Y = [int(i) for i in input().split()]
ans = 0

for i in range(1, 7):
  for j in range(1, 7):
    if i+j >= X or abs(i-j) >= Y:
      ans += 1

print(0 if ans/36 == 0 else ans/36)