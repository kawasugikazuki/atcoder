S = input()
T = input()
ans = 0
min_len = min(len(S),len(T))
error_flag = False

for i in range(min_len):
  if S[i] != T[i]:
    ans = i
    error_flag = True
    break
  # print(S[i],T[i])

if error_flag:
  print(ans+1)
elif len(S) != len(T):
  print(min_len+1)
else:
  print(ans)
