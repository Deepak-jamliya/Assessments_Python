'''
139Check if a string can be segmented into valid dictionary words. 
S = "applepenapple", Dict = ["apple", "pen"] TRUE

'''

s = "applepenapple"
dictionary = ["apple", "pen"]
n = len(s)
dp = [False] * (n + 1)
dp[0] = True
for i in range(1, n + 1):
    for word in dictionary:
        wl = len(word)
        if i >= wl and dp[i - wl] and s[i - wl:i] == word:
            dp[i] = True
print("Can be segmented:", dp[n])