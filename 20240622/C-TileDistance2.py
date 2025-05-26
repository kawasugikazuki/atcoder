# 不正解


# x_s,y_s=[int(i) for i in input().split()]
# x_g,y_g=[int(i) for i in input().split()]

# if (y_g-y_s<=0):
#   tmp_y=y_g
#   y_g=y_s
#   y_s=tmp_y
#   tmp_x=x_g
#   x_g=x_s
#   x_s=tmp_x

# plus_s=x_s+y_s
# plus_g=x_g+y_g
# diff_x=x_s-x_g
# diff_y=y_s-y_g
# step=0
# now_x=x_s
# now_y=y_s
# count=0
# flag=1

# # print(x_s,y_s)

# while step < abs(diff_x)+abs(diff_y)+1:
#   if (now_x == x_g and now_y == y_g):
#     print("ゴール")
#     break
#   if (diff_x <=0):
#     if now_y < y_g:
#       #偶数なら
#       now_y+=1
#       step+=1
#       count+=1
#       # print("右に詰まったから上")
#     elif now_x < x_g:
#       #奇数なら
#       now_x+=1
#       step+=1
#       # print("右")
#   else:
#     if now_y < y_g:
#       #奇数なら
#       now_y+=1
#       step+=1
#       count+=1
#       # print("左に詰まったから上")
#     elif now_x > x_g:
#       #偶数なら
#       now_x-=1
#       step+=1
#       # print("左")



# print(x_g,y_g)
# print(count)

