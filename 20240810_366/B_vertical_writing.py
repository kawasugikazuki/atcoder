N = int(input())
S=[""]*N
T_num=[]
# T=[]

for i in range(N):
  S[i]=input()
  T_num.append(len(S[i]))

# print(T_num)
T=[""]*max(T_num)
for i in range(N-1,-1,-1):
  for j in range(T_num[i]):
    print(i,j)
    print(S[i][j])
    T[j]+=S[i][j]

print(T)


