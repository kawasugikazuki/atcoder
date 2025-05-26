S = [int(s) for s in input()]
ans = len(S)
n = 0

for i in range(len(S)-1, -1, -1):
  n = n % 10
  tmp = (S[i] - n) % 10
  n += tmp
  ans += tmp

print(ans)

