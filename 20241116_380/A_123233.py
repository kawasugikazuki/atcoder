N = input()

cnt1 = 0
cnt2 = 0
cnt3 = 0
for s in N:
  if s == "1":
    cnt1 += 1
  elif s == "2":
    cnt2 += 1
  elif s == "3":
    cnt3 += 1

ans = "Yes" if cnt1 == 1 and cnt2 == 2 and cnt3 == 3 else "No"

print(ans)