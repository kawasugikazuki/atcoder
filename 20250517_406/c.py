N = int(input())
P = [int(i) for i in input().split()]

ans = 0

dx = []
for i in range(len(P)-1):
  if  P[i] - P[i+1] < 0:
    if not dx or dx[-1][0] == '-':
      dx.append(('+', 1))
    else:
      dx[-1] = ('+', dx[-1][1]+1)
  else:
    if not dx or dx[-1][0] == '+':
      dx.append(('-', 1))
    else:
      dx[-1] = ('-', dx[-1][1]+1)

# print(dx)

for i in range(1, len(dx)-1):
  if dx[i][0] == '-':
    ans += dx[i-1][1]*dx[i+1][1]
    
print(ans)