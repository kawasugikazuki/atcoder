A, B = [int(i) for i in input().split()]

dif = abs(A - B)

if dif == 0:
  print("1")
elif dif%2 == 0:
  print("3")
else:
  print("2")