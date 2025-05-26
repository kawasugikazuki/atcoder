N, D = [int(i) for i in input().split()]
eat_count = 0
S = list(input())

for i in range(len(S)-1, -1, -1):
  if S[i] == "@":
    S[i] = "."
    eat_count += 1
  if eat_count == D:
    break

print("".join(S))
    

