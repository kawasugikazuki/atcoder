Q = int(input())
M = 10**6 + 1

c = [0] * M
k = 0

for _ in range(Q):
  s = input()
  if s[0] == "1":
    _, x = map(int, s.split())
    if c[x] == 0:
      k += 1
    c[x] += 1
  elif s[0] == "2":
    _, x = map(int, s.split())
    c[x] -= 1
    if c[x] == 0:
      k -= 1
  else:
    print(k)