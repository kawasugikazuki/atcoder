# これだとTLEになる

# s = input()
# cheak=[]
# for i in range(len(s)-1,-1,-1):
#   cheak.append(s[i])
#   tmp = cheak[::-1]
#   ans = "".join(tmp)
#   if ans == "dream" or ans == "dreamer" or ans =="eraser" or ans == "erase":
#     cheak = []

# if len(cheak) ==0:
#   print("YES")
# else:
#   print("NO")

# 修正版

s = input()[::-1]

words = ["maerd","remaerd","resare","esare"]

index = 0
while index < len(s):
  matched = False
  for word in words:
    if s[index:index+len(word)] == word:
      matched = True
      index +=len(word)
      break
  if not matched:
    print("NO")
    exit()

print("YES")
