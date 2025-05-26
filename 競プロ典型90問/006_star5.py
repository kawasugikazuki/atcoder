from itertools import combinations

N, K = map(int,input().split())
S = input()
small_str = "z"*K
for i in combinations(S,K):
  now_str = "".join(map(str,i))
  if now_str < small_str:
    small_str = now_str

print(small_str)