Sx,Sy=[int(i) for i in input().split()]
Tx,Ty=[int(i) for i in input().split()]

# タイルの左側に揃える
Sx -= (Sx-Sy) % 2
Tx -= (Tx-Ty) % 2

# 原点に揃える
Tx -= Sx
Ty -= Sy

# 絶対値にする
Tx = abs(Tx) 
Ty = abs(Ty)


print(Ty+max(0,Tx-Ty) // 2)