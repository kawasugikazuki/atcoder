S = [int(s) for s in input()]
# print(S)
ans = 0

while S:
  if S[-1] != 0:
    for i in range(len(S)):
      if S[i] >= 1:
        S[i] -= 1
      else:
        S[i] = 9
    ans +=1
  else:
    S.pop()
    ans += 1

print(ans)