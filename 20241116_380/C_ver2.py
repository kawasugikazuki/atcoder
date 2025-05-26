N, K = [int(i) for i in input().split()]
S = input()

# 部分列の開始位置と終了位置を記録
index = [0] + [i for i in range(1, N) if S[i-1] != S[i]] +[N]
# 部分列に分解
splited_S = [S[index[i]:index[i+1]] for i in range(len(index)-1)]

if S[0] == '0':
  kth_1_index = 2*K-1
else:
  kth_1_index = 2*K-2

splited_S[kth_1_index-1], splited_S[kth_1_index] = splited_S[kth_1_index], splited_S[kth_1_index-1]

print("".join(splited_S))