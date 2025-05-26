a = int(input())
# b,c = [int(i) for i in input().split()]
# map関数の方が効率的(メモリ消費量が少なくなる)で一般的
b,c = map(int,input().split())
s = input()

print(a+b+c,s)