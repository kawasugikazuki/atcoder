# S,T = input().split(" ")
# # print(S,T)
# w = 0
# index = -1
# count = 0

# for i in range(len(S)):
#   # print(S[i])
#   if S[i] == T[0]:
#     index = i
#     break

# if index >=0:
#   w = index
#   for i in range(len(T)):
#     if T[i] == S[w]:
#       count += 1
#       w += index +1 


# if count == len(T) and index+1 != len(S):
#   print("Yes")
# else:
#   print("No")


# 入力を受け取る
S, T = input().split()

# SとTの長さを取得
len_S = len(S)
len_T = len(T)

# 条件を満たすcとwが存在するかを確認
found = False

for w in range(1, len_S):
    for c in range(1, w + 1):
        result = ""
        for i in range(0, len_S, w):
            if i + c - 1 < len_S:
                result += S[i + c - 1]
        if result == T:
            found = True
            break
    if found:
        break

# 結果を出力
if found:
    print("Yes")
else:
    print("No")
