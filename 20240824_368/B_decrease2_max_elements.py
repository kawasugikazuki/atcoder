# N = int(input())
# A = [int(i) for i in input().split()]
# count = 0
# checked_tag = True

# while checked_tag:
#   if sum(1 for num in A if num > 0) ==1:
#     checked_tag =False
#     break
#   A.sort(reverse=True)
#   A[0] -= 1
#   A[1] -= 1
#   count += 1
# print(count)

N = int(input())
A = [int(i) for i in input().split()]
count = 0

while True:
    # リストから最大値と2番目に大きい値を探す
    max1 = max(A)
    max1_index = A.index(max1)
    
    # 最大値を一時的に取り除いて、次に大きい値を探す
    A[max1_index] = float('-inf')  # 一時的に最小値に置き換え
    max2 = max(A)
    max2_index = A.index(max2)
    
    # 元の最大値を戻す
    A[max1_index] = max1
    
    # 終了条件
    if max1 == 0 or max2 == 0:
        break
    
    # 最大2つの値を減らす
    A[max1_index] -= 1
    A[max2_index] -= 1
    count += 1

print(count)
