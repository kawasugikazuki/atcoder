n,x,y = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

s =sorted(a,reverse=True)
t = sorted(b,reverse=True)
count_s = 0
count_t = 0
ans1=n
ans2=n
for i in range(n):
  count_s += s[i]
  if count_s >x:
    ans1=i+1
    break

for i in range(n):
  count_t += t[i]
  if count_t>y:
    ans2=i+1
    break
print(min(ans1,ans2))
