N = int(input())
S = [input() for _ in range(N)]

M = max(len(s) for s in S)
for i in range(N):
  S[i] += "*" * (M - len(S[i]))

T = [list(z)[::-1] for z in zip(*S)]
for t in T:
  while t[-1] == "*":
    t.pop()
  print("".join(t))
