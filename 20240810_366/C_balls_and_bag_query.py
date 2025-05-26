Q = int(input())
queries = [input().split() for _ in range(Q)]
numbers=set()
# print(queries[0])

for query in queries:
  if query[0] == "1":
    numbers.add(int(query[1]))
  elif query[0] == "2":
    numbers.discard(int(query[1]))
  elif query[0] == "3":
    print(len(numbers))
