N, S = [int(i) for i in input().split()]
T = [int(i) for i in input().split()]

is_sleep = False

if T[0] >= S + 0.5:
  is_sleep = True

for i in range(N-1):
  if T[i+1] - T[i] >= S + 0.5:
    is_sleep = True

print('Yes' if not is_sleep else 'No')