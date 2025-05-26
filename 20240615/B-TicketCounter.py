N,A=[int(i) for i in input().split()]
T=[int(i) for i in input().split()]
time=0

for i in range(N):
  if time<=T[i]:
    time=T[i]+A
    print(time)
  else:
    time+=A
    print(time)