from itertools import combinations

N,M=[int(i) for i in input().split()]
S=[""]*N
all_flavors=(1<<M)-1

for i in range(N):
  S[i]=input()

shop_flavors = []
for shop in S:
    flavor_bitset = 0
    for j in range(M):
        if shop[j] == 'o':
            flavor_bitset |= (1 << j)
    shop_flavors.append(flavor_bitset)


min_shops = N + 1
for i in range(1, N + 1):
    for combo in combinations(shop_flavors, i):
        combined_flavors = 0
        for flavor in combo:
            combined_flavors |= flavor
        if combined_flavors == all_flavors:
            min_shops = i
            break
    if min_shops != N + 1:
        break

print(min_shops)
