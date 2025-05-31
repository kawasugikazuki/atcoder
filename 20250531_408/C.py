N, M = [int(i) for i in input().split()]
wall_area = [0]*(N+1)

for i in range(M):
  l, r = [int(j) for j in input().split()]
  wall_area[l-1] += 1
  wall_area[r] -= 1

for i in range(1,N):
  wall_area[i] += wall_area[i-1]

print(min(wall_area[:-1]))