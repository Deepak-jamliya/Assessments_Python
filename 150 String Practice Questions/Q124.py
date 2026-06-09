'''
124Find the longest common subsequence of two strings. 
S1 = "AGGTAB", S2 = "GXTXAYB" 
"GTAB"

'''

s1 = "AGGTAB"
s2 = "GXTXAYB"

res = ""
j = 0

for ch in s1:
    while j < len(s2):
        if ch == s2[j]:
            res += ch
            j += 1
            break
        j += 1

print(res)