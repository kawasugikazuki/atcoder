R = input()
keta = R[0]

if int(R)<100:
  goal=100
else:
  goal = (int(keta)+1)*10**(len(R)-1)
print(goal-int(R))