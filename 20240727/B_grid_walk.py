h,w = [int(i) for i in input().split()]
x,y = [int(j) for j in input().split()]
x=x-1
y=y-1
grid = [""]*h
# print(grid)
for i in range(h):
  grid[i]=input()

command = input()

for i in command:
  if i =="U":
    # print("u")
    if x>0 and grid[x-1][y]==".":
      x-=1
      # print("u",x,y)
  elif i =="L":
    # print("l")
    if y>0 and grid[x][y-1]==".":
      y-=1
      # print("l",x,y)
  elif i =="R":
    # print("r")
    if y<w-1 and grid[x][y+1]==".":
      y+=1
      # print("r",x,y)
  else:
    # print("d")
    if x<h-1 and grid[x+1][y]==".":
      x+=1
      # print("d",x,y)

# print(grid)
# print(command)
print(x+1,y+1)