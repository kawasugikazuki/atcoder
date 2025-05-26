N, D = [int(i) for i in input().split()]
S = input()
air_count = 0

for s in S:
  if s == ".":
    air_count += 1

print(air_count+D)

