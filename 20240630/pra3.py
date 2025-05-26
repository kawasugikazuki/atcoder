# 入力を受け取る
n = int(input())
places = list(map(int, input().split()))
weights = list(map(int, input().split()))

# 場所ごとの荷物のリストを作成
from collections import defaultdict, Counter

place_dict = defaultdict(list)
for i in range(n):
    place_dict[places[i]].append(weights[i])

# 余分な荷物のリスト
extra_weights = []

# 各場所の荷物のリストを処理
for place in place_dict:
    place_weights = place_dict[place]
    if len(place_weights) > 1:
        # 最も軽い荷物以外をextra_weightsに追加
        place_weights.sort()
        extra_weights.extend(place_weights[:-1])

# 余分な荷物をソート
extra_weights.sort()

# 重複しない場所に荷物を移動するコストを計算
cost = 0
unique_places = len(place_dict)

# 必要な移動コストを計算
for weight in extra_weights:
    if unique_places < n:
        cost += weight
        unique_places += 1
    else:
        break

print(cost)
