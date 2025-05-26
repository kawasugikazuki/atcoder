A, B ,C = [int(i) for i in input().split()]

if B >= A and C <= A:
  print("Yes")
elif A <= B and C >= B:
  print("Yes")
elif A >= C and C >= B:
  print("Yes")
else:
  print("No")