N = int(input())
now =[0,0,0]
tag = True
for i in range(N):
  t,x,y = [int(j) for j in input().split()]
  diff_t=t-now[0]
  diff_x=abs(x-now[1])
  diff_y=abs(y-now[2])
  cheak =diff_t-diff_x-diff_y
  if cheak >= 0 and cheak %2 ==0:
    now =[t,x,y]
    # print(now)
  else:
    tag = False
    # print(now)

if tag:
  print("Yes")
else:
  print("No")