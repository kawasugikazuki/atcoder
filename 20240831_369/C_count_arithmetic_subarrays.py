# N = int(input())
# A = [int(i) for i in input().split()]

# count=0

# def check_array(array):
#   if len(array) <= 1:
#     return True
#   dif = array[1]-array[0]
#   for i in range(len(array)-1):
#     if array[i+1]-array[i] != dif:
#       return False
#   return True

# for i in range(N):
#   for j in range(i,N):
#     if check_array(A[i:j+1]) == True:
#       count+=1

# print(count)

N = int(input())
A = [int(i) for i in input().split()]

count = 0

def check_array(array):
    if len(array) <= 1:
        return True
    difference = array[1] - array[0]
    for i in range(1, len(array) - 1):
        if array[i + 1] - array[i] != difference:
            return False
    return True

for i in range(N):
    j = i  # jをiで初期化
    while j < N:
        # A[i:j+1]が等差数列かチェックし、等差数列ならカウントを増やし、jを増やす
        if check_array(A[i:j+1]):
            count += 1
            j += 1
        else:
            break  # 等差数列でなくなったら、その長さでのチェックをやめて次のiに移る

print(count)
