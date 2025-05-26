A, B = [int(i) for i in input().split()]

seisuu = A//B
amari = A/B - A//B
print(seisuu if amari < 0.5 else seisuu+1)