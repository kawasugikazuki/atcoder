Y = int(input())

if Y%4 ==0:
  # print("4の倍数")
  if Y%100!=0:
    print("366")
  if Y%100 ==0 and Y%400 !=0:
    print("365")
  if Y%400 ==0:
    print("366")
else:
  print("365")