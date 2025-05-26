N, K = [int(i) for i in input().split()]

R = [int(i) for i in input().split()]

import itertools

# 各数字の範囲を設定
ranges = [range(1, r + 1) for r in R]

# すべての組み合わせを生成
all_combinations = list(itertools.product(*ranges))

# 倍数になる組み合わせを見つける
valid_combinations = [comb for comb in all_combinations if sum(comb) % K == 0]

# 組み合わせを辞書順にソート
sorted_combinations = sorted(valid_combinations)

# 結果を表示
for comb in sorted_combinations:
    print(" ".join(map(str, comb)))

