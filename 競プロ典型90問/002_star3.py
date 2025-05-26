from itertools import product 

N = int(input())
def isValid(S):
  score=0
  for i in S:
    if i == "(":
      score +=1
    else:
      score -=1

    if score < 0:
      return False
  
  return score == 0

for i in product(["(",")"],repeat=N):
  if isValid(i):
    print(*i,sep="")
  