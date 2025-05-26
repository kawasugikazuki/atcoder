S = input()
sequence = 0
ans = []

for i,s in enumerate(S):
  if s == "-":
    sequence += 1
  elif i != 0 and s != "-":
    ans.append(sequence)
    sequence = 0

ans = [str(s) for s in ans]
print(" ".join(ans))