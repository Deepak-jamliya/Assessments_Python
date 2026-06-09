'''
148 Find the first recurring substring of length k.

S = "abcab", k = 2

'''

s = "abcab"
k = 2
seen = []
found = None
for i in range(len(s) - k + 1):
    sub = s[i:i+k]
    if sub in seen:
        found = sub
        break
    seen.append(sub)
print("First recurring substring of length", k, ":", found)