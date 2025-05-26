from bisect import bisect_left

# 入力の取得
box_num, buy_box_num = [int(i) for i in input().split()]
money_num = [int(i) for i in input().split()]
people_num = [int(i) for i in input().split()]

# ソートしておく
money_num.sort()
people_num.sort()

# 最小合計値を見つける
total_sum = 0
found = True

for num in people_num:
    index = bisect_left(money_num, num)
    if index < len(money_num):
        total_sum += money_num[index]
        money_num.pop(index)
    else:
        found = False
        break

if found and len(money_num) >= buy_box_num:
    print(total_sum)
else:
    print(-1)
