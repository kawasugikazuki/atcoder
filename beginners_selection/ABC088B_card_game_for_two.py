N = int(input())
a = [int(i) for i in input().split()]
a = sorted(a,reverse=True)
score1=0
score2=0
for i in range(N):
  if i % 2 == 0:
    score1+=a[i]
  else:
    score2+=a[i]

print(abs(score1-score2))