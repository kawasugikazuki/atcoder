N, K = [int(i) for i in input().split()]
S = list(input())
S.append("0")
sequence = 0
array = []

for i,s in enumerate(S):
  if s == "1":
    sequence += 1
  else:
    if sequence != 0:
      array.append((i-sequence,sequence))
      sequence = 0

# print(array)
kth_index, kth_len = array[K-1]
kth_part = S[kth_index:kth_index+kth_len]
tmp_part,tmp_len = array[K-2]
index = tmp_part+tmp_len
tmp_part = S[index:kth_index]
# print(tmp_part)
# print(kth_part)
S[index+kth_len:index+kth_len+len(tmp_part)] = tmp_part
# print(index+kth_len,index+kth_len+len(tmp_part))
S[index:index+kth_len] = kth_part
# print(index,index+kth_len)
# print(S)
del S[-1]
# print(S)
print("".join(S))
