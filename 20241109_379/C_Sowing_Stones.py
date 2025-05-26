N, M = [int(i) for i in input().split()]
X = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]


# def min_operations_to_distribute_stones(N, M, X, A):
#     # すべてのマスに0個の石が入っている状態を作成
#     stones = [0] * N
#     for i in range(M):
#         stones[X[i] - 1] = A[i]  # マスのインデックスに石の数を設定 (0始まり)

#     # 石の総数を確認し、N個でなければ不可能
#     total_stones = sum(stones)
#     if total_stones != N:
#         return -1

#     # 操作回数の累計と、各マスの差分を追跡するための変数
#     operations = 0
#     excess = 0  # 現在の過剰分または不足分

#     # 各マスで差を解消していく
#     for i in range(N):
#         excess += stones[i] - 1  # このマスでの過不足を更新
#         operations += abs(excess)  # 差分を操作回数に追加

#         # 右方向に移動できない場合（不足が補えない場合）は解決不可能
#         if excess < 0:
#             return -1

#     return operations

# print(min_operations_to_distribute_stones(N, M, X, A))

