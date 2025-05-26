A, B, C, D = [int(i) for i in input().split()]

deadline = A*60*60+B*60

submit_time = C*60*60+D*60

if submit_time < deadline:
  print("Yes")
else:
  print("No")