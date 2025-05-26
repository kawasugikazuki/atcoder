S = input()
ans_str=""
for i in range(1,4):
  ans_str += S[-i]

if ans_str == "nas":
  print("Yes")
else:
  print("No")
# print(ans_str)
