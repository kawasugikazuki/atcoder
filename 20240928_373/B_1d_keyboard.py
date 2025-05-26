S = input()
t = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
pre_str = "A"
count = 0
char_index_dict = {char: index for index, char in enumerate(S)}
for i in t:
  count += abs(char_index_dict[pre_str]-char_index_dict[i])
  pre_str = i

print(count)