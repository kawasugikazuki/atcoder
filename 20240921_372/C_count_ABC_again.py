N, Q = [int(i) for i in input().split()]
S = list(input())
ans = 0

for i in range(N-2):
  if S[i] == "A" and S[i+1] == "B" and S[i+2] == "C":
    ans += 1

for _ in range(Q):
  x,c = input().split()
  x = int(x)-1
  for i in range(3):
    idx = x - i
    if S[idx] == "A" and S[idx+1] == "B" and S[idx+2] == "C":
      ans -= 1
  S[x] = c
  for i in range(3):
    idx = x - i
    if S[idx] == "A" and S[idx+1] == "B" and S[idx+2] == "C":
      ans += 1

  print(ans)


  