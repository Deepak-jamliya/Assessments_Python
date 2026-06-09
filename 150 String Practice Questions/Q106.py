'''
106Generate all subsequences of a string. 
S = "ab" 
"", "a", "b", "ab"

'''

s = "ab"
res = [""]

for ch in s:
    res += [x + ch for x in res]

print(res)