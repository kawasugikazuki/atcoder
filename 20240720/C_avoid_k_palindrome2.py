from itertools import permutations

def count_non_palindromic_permutations(s, k):
    # すべての順列を生成
    perms = set(permutations(s))
    count = 0

    # 回文かどうかをチェックする関数
    def is_palindrome(sub):
        return sub == sub[::-1]
    
    for perm in perms:
        perm_str = ''.join(perm)
        has_palindrome = False
        # 長さ k の部分文字列をチェック
        for i in range(len(perm_str) - k + 1):
            if is_palindrome(perm_str[i:i + k]):
                has_palindrome = True
                break
        if not has_palindrome:
            count += 1
    
    return count

N,K = [int(i) for i in input().split()]
S = input()
result = count_non_palindromic_permutations(S, K)
print(result)