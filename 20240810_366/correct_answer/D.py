N = int(input())
A=[]
for _ in range(N):
  a = [list(map(int,input().split())) for _ in range(N)]
  A.append(a)

# print(A)

Q = int(input())
for _ in range(Q):
  lx,rx,ly,ry,lz,rz = map(int,input().split())
  print(lx,rx,ly,ry,lz,rz)
  # print(A[][][])