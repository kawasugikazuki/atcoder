A=[0,1,2,3,2,3]

ans = 0
for i in range(len(A)-2):
  # 真の時1加える
  ans += A[i] == A[i+2]

print(ans)
