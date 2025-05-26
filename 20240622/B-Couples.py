N = int(input())
A = [0]*2*N
A = [ int(i) for i in input().split()]
count=0

for i in range(N):
  first_index,second_index = [j for j, x in enumerate(A) if (i + 1)== x]
  if ( second_index - first_index   ==2):
    count += 1
  
print(count)

