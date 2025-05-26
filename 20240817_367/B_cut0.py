X = float(input())
formatted_number = f"{X:.10f}".rstrip('0').rstrip('.')
print(formatted_number)