# N = int(input())
# H = [int(i) for i in input().split()]

# count = 0
# checked_index = 0

# while checked_index < N:
#     # 今のindexのH[checked_index]が0以下になるまでループ
#     if count % 3 == 2:  # countが3の倍数なら3を引く
#         H[checked_index] -= 3
#     else:  # それ以外は1を引く
#         H[checked_index] -= 1
    
#     count += 1
    
#     # H[checked_index]が0以下になったら次の要素に移動
#     if H[checked_index] <= 0:
#         checked_index += 1

# できなかった
N = int(input())
H = [int(i) for i in input().split()]

T = 0

for i in H:
  num = i//5
  T += num*3
  a = i-num*5
  while a>0:
    T += 1
    if T%3 ==0:
      a -= 3
    else:
      a -=1

print(T)