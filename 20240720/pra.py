from collections import Counter

def is_palindromic(sub):
    return sub == sub[::-1]

def generate_permutations(s, k, path, counter, result):
    if len(path) == len(s):
        result.append("".join(path))
        return
    
    for char in counter:
        if counter[char] > 0:
            if len(path) >= k - 1 and is_palindromic(path[-(k-1):] + [char]):
                continue
            
            counter[char] -= 1
            path.append(char)
            generate_permutations(s, k, path, counter, result)
            path.pop()
            counter[char] += 1

def count_permutations_without_k_length_palindrome(s, k):
    counter = Counter(s)
    result = []
    generate_permutations(s, k, [], counter, result)
    return len(result)

# Input
N, K = map(int, input().split())
S = input()

# Calculate and print the result
result = count_permutations_without_k_length_palindrome(S, K)
print(result)
