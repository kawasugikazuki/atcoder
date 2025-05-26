# 入力を受け取る
n = int(input())
places = list(map(int, input().split()))
weights = list(map(int, input().split()))

# 場所ごとの荷物のリストを作成
from collections import defaultdict

place_dict = defaultdict(list)
for i in range(n):
    place_dict[places[i]].append(weights[i])

# 各場所の荷物のリストをソート（軽い順）
for place in place_dict:
    place_dict[place].sort()

# 重複している場所の荷物の移動コストを計算
cost = 0
all_weights = []

for place in place_dict:
    while len(place_dict[place]) > 1:
        weight = place_dict[place].pop(0)
        all_weights.append(weight)

# 重複しない場所に荷物を移動するコストを計算
for weight in all_weights:
    cost += weight

print(cost)
