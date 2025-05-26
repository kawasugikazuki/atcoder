def f(l, r, k):
    res = 0
    while l + 1 < r:
        c = (l + r) // 2
        if k < c:
            r = c
        else:
            l = c
            res += 1
    return res

def flip(c):
    if c.islower():
        return chr(ord(c) - ord('a') + ord('A'))
    return chr(ord(c) - ord('A') + ord('a'))

def main():
    s = input().strip()  # 文字列
    n = len(s)
    q = int(input().strip())  # クエリ数
    queries = list(map(int, input().strip().split()))  # クエリのリスト
    results = []
    
    for k in queries:
        k -= 1  # 0-based index に調整
        si = k % n
        k //= n
        cnt = f(0, 1 << 60, k)
        ans = s[si]
        if cnt % 2:
            ans = flip(ans)
        results.append(ans)
    
    print("".join(results))

if __name__ == "__main__":
    main()
