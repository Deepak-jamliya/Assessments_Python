'''
113Find the minimum number of insertions to make a string palindrome. 
S = "aebcbda" 
2 (insert 'd', 'e' → "adebcbeda")

'''

s = input("Enter String = ")
n = len(s)

dp = [1] * n

for i in range(n - 2, -1, -1):
    prev = 0
    for j in range(i + 1, n):
        temp = dp[j]
        if s[i] == s[j]:
            dp[j] = prev + 2
        else:
            dp[j] = max(dp[j], dp[j - 1])
        prev = temp

print(n - dp[n - 1])