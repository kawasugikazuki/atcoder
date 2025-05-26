N = int(input())
A = [int(i) for i in input().split()]
B=sorted(A,reverse=True)
print(A.index(B[1])+1)
