S = input()

R_index = 0
M_index = 0
for i in range(len(S)):
  if S[i] == "R":
    R_index = i
  elif S[i] == "M":
    M_index =i

if R_index < M_index:
  print("Yes")
else:
  print("No")